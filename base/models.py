from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class House(models.Model):
    title = models.CharField(max_length=100)	
    date_posted = models.DateTimeField(default=timezone.now)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
	    return self.title

class Blog(models.Model):
    author = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateField(default=timezone.now)

    def __str__(self):
         return self.name

