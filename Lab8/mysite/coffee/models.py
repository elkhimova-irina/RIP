from django.db import models

# Create your models here.

class coffee(models.Model):
    img = models.ImageField(upload_to = 'images', null=True, blank = True)
    type = models.CharField(max_length = 50, blank=True, unique = True)
    intro = models.CharField(max_length = 300, blank=True)
    about = models.TextField(blank=True)