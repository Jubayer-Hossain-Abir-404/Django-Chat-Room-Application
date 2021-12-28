from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

rooms1 = [
    {'id': 1, 'name': 'Lets learn python'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend Developers'},
]


#request object is going to be like the http object
# return HttpResponse ('Home Page') # this returns html code directly
def home(request):
    return render(request, 'home.html', {'rooms': rooms1}) 

def rooms(request):
    # return HttpResponse('Room')
    return render(request, 'room.html')
