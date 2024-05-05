from django.db import models

# Create your models here.

from django.db import models


class Conversation(models.Model):
    sender = models.CharField(max_length=15)
    message = models.CharField(max_length=5000)
    response = models.CharField(max_length=5000)
