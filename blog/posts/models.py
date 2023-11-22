from django.db import models

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_publishd = models.BooleanField(default=False)
    publishd_at = models.DateTimeField()
    
    
