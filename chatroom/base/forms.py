from django.forms import ModelForm
from .models import Room


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
        fields = '__all__'
