from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.CharField(max_length=200) 
    comment = models.CharField(max_length=200) 