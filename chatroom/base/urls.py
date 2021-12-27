from django.urls import path
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="home"),  # here keeping name="home" is a good practice
    path('room/', views.rooms, name="rooms"), # calling rooms function from views
    
]