from django.db import models

# Create your models here.

class blog(models.Model):

    name = models.CharField(max_length=2048)
    plot = models.TextField()
    rating = models.BooleanField()
    release_date = models.DateField()
