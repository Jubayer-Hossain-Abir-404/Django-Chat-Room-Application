from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

#request object is going to be like the http object
def home(request):
    return HttpResponse ('Home Page')
      


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
