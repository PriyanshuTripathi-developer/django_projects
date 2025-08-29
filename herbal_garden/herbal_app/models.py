from django.db import models

class Herb(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=150)
    description = models.TextField()
    ailments = models.TextField(help_text="Comma-separated ailments")
    growth_conditions = models.TextField()
    image = models.ImageField(upload_to='herbs/')

    def __str__(self):
        return self.name
