from django.db import models

# Create your models here.

class UserMessage(models.Model):
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=250)
    email = models.EmailField()
    name = models.CharField(max_length=50)