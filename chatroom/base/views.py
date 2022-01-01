from django.shortcuts import render, redirect
from .models import Room, Topic
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
    # inline if statement
    # it's going to be checked if the request method has something
    # if q!=None then q is the parameter
    # else q is going to be an empty string

    q= request.GET.get('q') if request.GET.get('q') != None else ''
    # rooms1 = Room.objects.all() #this will give all the room in the database

    # icontains i is case insensitive
    # it's going to make sure whatever value we have in the topic name atleast
    # in here
    # for example if q contains only py. It's still going to return a positive
    # match
    # if no parameter. technically all of the parameters match
    rooms1 = Room.objects.filter(topic__name__icontains=q) 

    topics = Topic.objects.all()

    context = {'rooms': rooms1, 'topics': topics}
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


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    # this prefills the value
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method =='POST':
        # simply gonna remove that item
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})

