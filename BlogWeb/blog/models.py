from django.db import models

# Create your models here.
class Blog(models.Model):
    title =models.CharField(max_length=256, default="")
    content= models.TextField(default="")
    is_published =models.BooleanField(default=False)
    published_at =models.DateTimeField(null=True , blank=True)
