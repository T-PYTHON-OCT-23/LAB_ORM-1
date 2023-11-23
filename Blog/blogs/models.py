from django.db import models

# Create your models here.

class Blogs(models.Model):
    categories = models.TextChoices("categories",["Action","Fantacy","Horror","Romantic"])

    title = models.CharField(max_length=2048)
    name_publisher = models.CharField(max_length=2048,null=True)
    published_location = models.CharField(max_length=1024,null=True)
    content = models.TextField()
    is_published = models.BooleanField()
    published_at = models.DateTimeField()
    catagory = models.CharField(max_length=1028,choices=categories.choices)
    images = models.ImageField(upload_to="images/",default="/images/mainlogo.png")