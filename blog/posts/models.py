from django.db import models

# Create your models here.

class posts(models.Model):

    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_publishd = models.BooleanField(default=False)
    publishd_at = models.DateTimeField()
    
    def __str__(self):
        return self.title
