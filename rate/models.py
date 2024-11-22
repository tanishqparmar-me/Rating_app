from django.db import models

class user(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class rating(models.Model):
    name = models.CharField(max_length=100)
    rate = models.CharField(max_length=100)
    message = models.CharField(max_length=300)