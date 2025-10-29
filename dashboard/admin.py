from django.contrib import admin
from .models import Location, WeatherData


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'latitude', 'longitude', 'is_active', 'created_at']
    list_filter = ['is_active', 'country', 'created_at']
    search_fields = ['name', 'country']


@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ['location', 'temperature', 'humidity', 'description', 'recorded_at']
    list_filter = ['location', 'recorded_at']
    search_fields = ['location__name', 'description']
    date_hierarchy = 'recorded_at'