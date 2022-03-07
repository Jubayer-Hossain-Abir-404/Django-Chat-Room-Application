from django.forms import ModelForm
from .models import Room, User
# from django.contrib.auth.models import User


# The tradition is here to specify the model name and then form
# This is going to inherit from Model Form
class RoomForm(ModelForm):
    # When meta data is being set 
    class Meta:
        # the model is going to be set for which the form is created for
        model = Room
        # specify the field
        # this will create the form based on the metadata of this room right here
        # the non-editable fields won't show up 
        # basically creating a form based on all those values
        # it's going to be give all those values
        # hide values like the user because that should be auto-genarated
        # like the logged in user that creates the application should know
        # a user shouldn't be able to specify who they are necessarily in a
        # drop-down menu
        fields = '__all__' # Currently it is just giving all the fields

        # This is how fields can be excluded
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        # this is the user model
        model = User
        # here it is supposed to be fields
        # the fields which are going to stay
        # in the form field
        fields = ['username', 'email']
