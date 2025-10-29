from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.conf import settings
from django.db.models import Avg, Max, Min, Count
import requests

from .models import Location, WeatherData
from .serializers import LocationSerializer, WeatherDataSerializer, WeatherStatsSerializer
from django.shortcuts import render


def index(request):
    """
    Homepage view
    """
    return render(request, 'dashboard/index.html')

class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoints for CRUD operations on Locations
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    @action(detail=True, methods=['get'])
    def current_weather(self, request, pk=None):
        """
        Get current weather for a specific location from OpenWeatherMap API
        """
        location = self.get_object()
        
        # OpenWeatherMap API call
        api_key = settings.OPENWEATHER_API_KEY
        url = f"{settings.OPENWEATHER_BASE_URL}/weather"
        params = {
            'lat': location.latitude,
            'lon': location.longitude,
            'appid': api_key,
            'units': 'metric'
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            weather_data = response.json()
            
            # Save to database for analytics
            WeatherData.objects.create(
                location=location,
                temperature=weather_data['main']['temp'],
                feels_like=weather_data['main']['feels_like'],
                humidity=weather_data['main']['humidity'],
                pressure=weather_data['main']['pressure'],
                wind_speed=weather_data['wind']['speed'],
                description=weather_data['weather'][0]['description'],
                icon=weather_data['weather'][0]['icon']
            )
            
            return Response({
                'location': location.name,
                'temperature': weather_data['main']['temp'],
                'feels_like': weather_data['main']['feels_like'],
                'humidity': weather_data['main']['humidity'],
                'pressure': weather_data['main']['pressure'],
                'wind_speed': weather_data['wind']['speed'],
                'description': weather_data['weather'][0]['description'],
                'icon': weather_data['weather'][0]['icon']
            })
        
        except requests.exceptions.RequestException as e:
            return Response(
                {'error': f'Failed to fetch weather data: {str(e)}'}, 
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )

    @action(detail=False, methods=['get'])
    def search_city(self, request):
        """
        Search for a city using OpenWeatherMap Geocoding API
        """
        city_name = request.query_params.get('city', '')
        
        if not city_name:
            return Response(
                {'error': 'City name is required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        api_key = settings.OPENWEATHER_API_KEY
        url = "http://api.openweathermap.org/geo/1.0/direct"
        params = {
            'q': city_name,
            'limit': 5,
            'appid': api_key
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            cities = response.json()
            
            results = [{
                'name': city['name'],
                'country': city['country'],
                'latitude': city['lat'],
                'longitude': city['lon'],
                'state': city.get('state', '')
            } for city in cities]
            
            return Response(results)
        
        except requests.exceptions.RequestException as e:
            return Response(
                {'error': f'Failed to search city: {str(e)}'}, 
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )


class WeatherDataViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoints for viewing weather data (read-only)
    """
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer

    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """
        Get weather statistics grouped by location
        Data visualization endpoint
        """
        stats = Location.objects.annotate(
            total_records=Count('weather_records'),
            avg_temperature=Avg('weather_records__temperature'),
            max_temperature=Max('weather_records__temperature'),
            min_temperature=Min('weather_records__temperature'),
            avg_humidity=Avg('weather_records__humidity')
        ).filter(total_records__gt=0).values(
            'name', 'total_records', 'avg_temperature', 
            'max_temperature', 'min_temperature', 'avg_humidity'
        )
        
        serializer = WeatherStatsSerializer(stats, many=True)
        return Response(serializer.data)