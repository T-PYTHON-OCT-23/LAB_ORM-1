from django.db import models

# Create your models here.

class Blogs(models.Model):

    title = models.CharField(max_length=2048)
    name_publisher = models.CharField(max_length=2048,null=True)
    published_location = models.CharField(max_length=1024,null=True)
    content = models.TextField()
    is_published = models.BooleanField()
    published_at = models.DateTimeField()