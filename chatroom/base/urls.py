from django.urls import path
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="home"),  # here keeping name="home" is a good practice
    path('room/<str:pk>/', views.rooms, name="rooms"), # calling rooms function from views

    path('create-room/', views.createRoom, name="create-room"),
    
]