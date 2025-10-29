from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet, WeatherDataViewSet

router = DefaultRouter()
router.register(r'locations', LocationViewSet, basename='location')
router.register(r'weather-data', WeatherDataViewSet, basename='weather-data')

urlpatterns = [
    path('', include(router.urls)),
]