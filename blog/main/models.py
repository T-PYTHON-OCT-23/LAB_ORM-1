from django.db import models
from .models import blog

# Create your models here.


class blog(models.Model):
    name = models.CharField(max_length=512)
    paragraph = models.TextField()
    release_date = models.DateField()
