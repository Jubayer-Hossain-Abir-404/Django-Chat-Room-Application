from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm
# from django.http import HttpResponse

# Create your views here.

# rooms1 = [
#     {'id': 1, 'name': 'Lets learn python'},
#     {'id': 2, 'name': 'Design with me'},
#     {'id': 3, 'name': 'Frontend Developers'},
# ]


#request object is going to be like the http object
# return HttpResponse ('Home Page') # this returns html code directly
def home(request):
    rooms1 = Room.objects.all() #this will give all the room in the database
    context = {'rooms': rooms1}
    return render(request, 'base/home.html', context) 

def rooms(request, pk):
    # return HttpResponse('Room')
    # room = None
    # for i in rooms1:
    #     if i['id'] == int(pk):
    #         room = i

    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)


def createRoom(request):
    form = RoomForm()
    
    if request.method == 'POST':
        # This prints all the data in the backend
        # print(request.POST)  # here POST is all the data
        form = RoomForm(request.POST)
        # checks if the form is valid
        if form.is_valid():
            # saves the form data
            form.save()
            # then the form will be redirected to the home
            return redirect('home')


    
    context = {'form': form}
    return render(request, 'base/room_form.html',context)
