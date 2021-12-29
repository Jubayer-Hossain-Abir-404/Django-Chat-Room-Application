from django.db import models

# Create your models here.

class Room(models.Model):
    # host = 
    # topic =
    name= models.CharField(max_length=200) # Meaning this can't be blank
                                           # for that null is false
    description = models.TextField(null=True, blank=True) 
    # here textfield true. can be blank
    # it means when form is submitted description can be blank
    # participants = 
    # all the participants will be kept in there
    updated = models.DateTimeField(auto_now=True) 
    # this will change everytime instance is saved 
    created = models.DateTimeField(auto_now_add=True)
    # this will be set at the very begining and never change again


    def __str__(self):
        return self.name  #This will return name

