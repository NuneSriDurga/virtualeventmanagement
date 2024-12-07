from django.db import models
from django.contrib.auth.models import User

class EventList(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name

from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    description = models.TextField()

    def __str__(self):
        return self.name