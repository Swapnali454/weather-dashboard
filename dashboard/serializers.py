from rest_framework import serializers
from .models import Location, WeatherData


class LocationSerializer(serializers.ModelSerializer):
    """
    Serializer for Location model - handles CRUD operations
    """
    weather_records_count = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = ['id', 'name', 'country', 'latitude', 'longitude', 
                  'created_at', 'updated_at', 'is_active', 'weather_records_count']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_weather_records_count(self, obj):
        return obj.weather_records.count()


class WeatherDataSerializer(serializers.ModelSerializer):
    """
    Serializer for WeatherData model
    """
    location_name = serializers.CharField(source='location.name', read_only=True)

    class Meta:
        model = WeatherData
        fields = ['id', 'location', 'location_name', 'temperature', 'feels_like', 
                  'humidity', 'pressure', 'wind_speed', 'description', 'icon', 'recorded_at']
        read_only_fields = ['id', 'recorded_at']


class WeatherStatsSerializer(serializers.Serializer):
    """
    Serializer for weather statistics/analytics
    """
    name = serializers.CharField()  # Changed from location_name to name
    avg_temperature = serializers.FloatField()
    max_temperature = serializers.FloatField()
    min_temperature = serializers.FloatField()
    avg_humidity = serializers.FloatField()
    total_records = serializers.IntegerField()