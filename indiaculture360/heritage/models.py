from django.db import models

class HeritageSite(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    era = models.CharField(max_length=100)
    site_type = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    image_url = models.URLField()
    audio_url = models.URLField(blank=True)
    video_url = models.URLField(blank=True, null=True)
    
    
    def __str__(self):
        return self.name

