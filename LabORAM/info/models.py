from django.db import models

# Create your models here.

class Info(models.Model):
    title = models.CharField(max_length=2000)
    contant = models.TextField()
    is_published= models.BooleanField()
    published_at = models.DateField()



