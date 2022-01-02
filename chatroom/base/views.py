from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        # checking if the user info is correct
        user =authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'Username or password is incorrect')



    context ={}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')

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
    rooms1 = Room.objects.filter(
        Q(topic__name__icontains=q) | 
        Q(name__icontains=q) |
        Q(description__icontains=q)
        
        ) 

    topics = Topic.objects.all()
    room_count = rooms1.count()

    context = {'rooms': rooms1, 'topics': topics, 'room_count':room_count}
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

# if an user is not authenticated then access will not be provided
@login_required(login_url='login')
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

@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    # this prefills the value
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')


    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')
        
    if request.method =='POST':
        # simply gonna remove that item
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})

