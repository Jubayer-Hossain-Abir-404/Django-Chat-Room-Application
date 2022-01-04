from django.db import models
from django.contrib.auth.models import User # built in way of creating a user

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    # Somebody has to host a room and then a topic
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # It needs to be allowed set null=True
    # Because when the parent table gets removed and set to null it should 
    # be made sure that the database will allow it
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name= models.CharField(max_length=200) # Meaning this can't be blank
                                           # for that null is false
    description = models.TextField(null=True, blank=True)
    # This is a many to many relationship
    # Issue is there is already a user model connected
    # related name 
    # can't reference a user because it's already up in there
    # that's why the related name here is going to be participants
    # blank=true. Also want to submit a form without having to check
    # something
    participants = models.ManyToManyField(User,related_name='participants', blank=True)
    # here textfield true. can be blank
    # it means when form is submitted description can be blank
    # participants = 
    # all the participants will be kept in there
    updated = models.DateTimeField(auto_now=True) 
    # this will change everytime instance is saved 
    created = models.DateTimeField(auto_now_add=True)
    # this will be set at the very begining and never change again

    class Meta:
        ordering = ['-updated', '-created']


    def __str__(self):
        return self.name  #This will return name


class Message(models.Model):
    # This is going to be a one to many relationship
    # user can have many messages
    # whereas messages can have one user
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     room = models.ForeignKey(Room, on_delete=models.CASCADE)
     body = models.TextField()
     updated = models.DateTimeField(auto_now=True) 
     created = models.DateTimeField(auto_now_add=True)

     class Meta:
        ordering = ['-updated', '-created']

    

     def __str__(self):
         return self.body[0:50] # for the first 50 characters



