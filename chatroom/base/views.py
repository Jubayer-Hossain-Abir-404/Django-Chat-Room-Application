from pydoc_data.topics import topics
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Room, Topic, Message, User
from .forms import RoomForm, UserForm

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

    # This is used so that user can't login again when the user is already
    # logged in

    page= 'login'
    if request.user.is_authenticated:
        return redirect('home')


    if request.method == 'POST':
        # user name has to be in lower case 
        # username = request.POST.get('username').lower()
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=username)
        except:
            messages.error(request, 'User does not exist')

        # checking if the user info is correct
        user =authenticate(request, email=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'Username or password is incorrect')



    context ={'page': page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    # page = 'register'
    # Django provided user creation form
    form = UserCreationForm()
    # context ={'page': page}
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # saving this form but freezing it in time
            user = form.save(commit=False)
            # cleaning the data
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
    return render(request, 'base/login_register.html', {'form': form})

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


    # this will give the first five topics
    topics = Topic.objects.all()[0:5]
    room_count = rooms1.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))

    context = {'rooms': rooms1, 'topics': topics, 'room_count':room_count, 
    'room_messages': room_messages}
    return render(request, 'base/home.html', context) 

def rooms(request, pk):
    # return HttpResponse('Room')
    # room = None
    # for i in rooms1:
    #     if i['id'] == int(pk):
    #         room = i

    room1 = Room.objects.get(id=pk)
    # child objects of a specific room can be querid here
    # set of messages that are related to the specific room is gonna be provided
    # Descending order based on created
    room_messages = room1.message_set.all()
    # For a many to many to relation .all() is enough
    participants= room1.participants.all()
    if request.method == 'POST':
        # create method will go over there and create an actual message
        message = Message.objects.create(
            user = request.user,
            room = room1,
            body= request.POST.get('body')
        )
        room1.participants.add(request.user)
        # here rooms is coming from the url name="rooms"
        return redirect('rooms', pk=room1.id)

    context = {'room': room1, 'room_messages': room_messages, 
    'participants': participants}
    return render(request, 'base/room.html', context)

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    # All the children of a specific object can be get by doing 
    # the model name and underscore set and whatever we want there
    # In this case all of them is being fetched here
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    # context dictionary
    # As the code has been split into many parts 
    # the variable has to be same in components all over
    # otherwise it will not work
    context = {'user': user, 'rooms': rooms, 'room_messages': room_messages,
    'topics': topics}
    return render(request, 'base/profile.html', context)

# if an user is not authenticated then access will not be provided
@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    topics = Topic.objects.all()
    if request.method == 'POST':
        # This prints all the data in the backend
        # print(request.POST)  # here POST is all the data
        topic_name = request.POST.get('topic')
        # get or create is a method
        # it's gonna return back either an object
        # or it will return an object and created
        # and whats going to happen is that if the topic
        # name is passed for the name value so
        # if the topic is found in the database then topic
        # will be true like python but a new topic is created
        # like java then created will be true and new topic 
        # will be created
        topic, created = Topic.objects.get_or_create(name=topic_name)

        Room.objects.create(
            host=request.user,
            topic = topic,
            name= request.POST.get('name'),
            description = request.POST.get('description')
        )
        # form = RoomForm(request.POST)
        # checks if the form is valid
        # if form.is_valid():
            # Here commit is false. That's gonna give an instance of this room 
            # Here what happens is that the saved form instance is saved in
            # room. after that the current user gets saved to room.host and
            # then saved
            # room = form.save(commit=False)
            # room.host = request.user
            # room.save()
            # saves the form data
            # form.save()
            # then the form will be redirected to the home

        return redirect('home')


    
    context = {'form': form, 'topics': topics}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    # this prefills the value
    form = RoomForm(instance=room)
    topics = Topic.objects.all()

    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')


    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        # form = RoomForm(request.POST, instance=room)
        # if form.is_valid():
        #     form.save()
        # here we are gonna get the name
        # and update it
        room.name = request.POST.get('name')
        # here the topic could be newly created topic
        # or the previous one
        room.topic = topic
        room.description = request.POST.get('description')
        # all the value will be taken and 
        # then saved
        room.save()
        return redirect('home')

    context = {'form': form, 'topics': topics, 'room': room}
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


@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse('You are not allowed here!!')

    if request.method =='POST':
        # simply gonna remove that item
        message.delete()
        return redirect('home')
    # This template is supposed to be dynamic
    return render(request, 'base/delete.html', {'obj': message})


@login_required(login_url='login')
def updateUser(request):

    # this instance is going to give the
    # initial user value
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, instance= user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)
    return render(request, 'base/update-user.html', {'form': form})


def topicsPage(request):
    q= request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains=q)
    return render(request, 'base/topics.html', {'topics':topics})


def activityPage(request):
    room_messages = Message.objects.all()
    return render(request, 'base/activity.html', {'room_messages': room_messages})

