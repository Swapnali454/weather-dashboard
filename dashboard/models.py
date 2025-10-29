from django.db import models
from django.utils import timezone


class Location(models.Model):
    """
    Model to store user's favorite locations for weather tracking
    """
    name = models.CharField(max_length=100, help_text="City name")
    country = models.CharField(max_length=100, help_text="Country name")
    latitude = models.FloatField(help_text="Latitude coordinate")
    longitude = models.FloatField(help_text="Longitude coordinate")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, help_text="Is location active for tracking")

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        return f"{self.name}, {self.country}"


class WeatherData(models.Model):
    """
    Model to store historical weather data for analytics
    """
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='weather_records')
    temperature = models.FloatField(help_text="Temperature in Celsius")
    feels_like = models.FloatField(help_text="Feels like temperature")
    humidity = models.IntegerField(help_text="Humidity percentage")
    pressure = models.IntegerField(help_text="Atmospheric pressure")
    wind_speed = models.FloatField(help_text="Wind speed in m/s")
    description = models.CharField(max_length=200, help_text="Weather description")
    icon = models.CharField(max_length=10, help_text="Weather icon code")
    recorded_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-recorded_at']
        verbose_name = 'Weather Data'
        verbose_name_plural = 'Weather Data'

    def __str__(self):
        return f"{self.location.name} - {self.temperature}°C at {self.recorded_at}"