from django.db import models

# Create your models here.
class Web (models.Model):
   Title = models.CharField(max_length=2048) 
   Contant =models.TextField()
   is_published =models.BooleanField()
   published_at = models.DateTimeField()