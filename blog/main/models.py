from django.db import models
from datetime import date


# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=512)
    paragraph = models.TextField(default='--')
    release_date = models.DateField(auto_now=True)
