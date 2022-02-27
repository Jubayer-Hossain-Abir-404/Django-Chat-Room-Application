# in order to hit the endpoint this
# urls.py file is going to be required

from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('rooms/', views.getRooms)
]