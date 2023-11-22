from django.db import models


class Blog(models.Model):
    title=models.CharField(max_length=300)
    content=models.TextField()
    is_published=models.BooleanField()
    published_at=models.DateField()