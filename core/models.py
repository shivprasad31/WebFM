from django.db import models

# Create your models here.
class Stations(models.Model):
    name=models.CharField(max_length=100)
    stream_url=models.URLField()
    frequency=models.CharField(max_length=20,blank=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
