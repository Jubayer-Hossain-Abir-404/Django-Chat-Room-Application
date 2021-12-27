from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

#request object is going to be like the http object
def home(request):
    # return HttpResponse ('Home Page') # tis returns html code directly
    return render(request, 'home.html') # as template has been configured 
                                        # now it can get the file directly and request is the object


def rooms(request):
    # return HttpResponse('Room')
    return render(request, 'room.html')
