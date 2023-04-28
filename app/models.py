from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField('img',default='default.jpg',upload_to='Resource/users/')
    conversation =models.ManyToManyField('Conversation',blank=True)
    objects = models.Manager()
    
    def __str__(self):
        return str(self.user)
    
    
class Room(models.Model):
    members=models.ManyToManyField(Profile,blank=True)
    objects = models.Manager()

    
class Message(models.Model):
    value = models.CharField(max_length=7000)
    time = models.DateTimeField(default=datetime.now,blank=True)
    room = models.ForeignKey(Room,related_name='Message',on_delete=models.CASCADE,null=True)
    user = models.CharField(max_length=7000)


class Conversation(models.Model):
    name = models.CharField(max_length=7000)
    room = models.ForeignKey(Room,related_name='Conversation',on_delete=models.CASCADE,null=True)
    avatar = models.ImageField(default='default.jpg',upload_to='Resource/users/')