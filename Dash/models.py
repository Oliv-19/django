from django.db import models
from datetime import datetime

# Create your models here.
class Users(models.Model):
    user = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    pic = models.ImageField(upload_to='media', null=True)

class Room(models.Model):
    room_name = models.CharField(max_length=100)

class Users_Rooms(models.Model):
    users_id =models.CharField(max_length=100000)
    rooms_id= models.CharField(max_length=100000)

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    user = models.CharField(max_length=10, default=str)
    room = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now(), blank=True)