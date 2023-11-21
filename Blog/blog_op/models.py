from django.db import models

# Create your models here.

class Published(models.Model):
    
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_published = models.BooleanField()
    published_at = models.DateField()
