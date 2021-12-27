from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#request object is going to be like the http object
def home(request):
    return HttpResponse ('Home Page')


def rooms(request):
    return HttpResponse('Room')
