# from webbrowser import get
# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer

# This is going to be in views that
# shows all the routes in our APi

# GET, PUT, POST methods can be used 
# here
@api_view(['GET'])
def getRoutes(request):
    # url or routes are gonna be two get
    # methods
    # this is a json response
    routes = [
        # so if you are going for GET
        # you are gonna get this home page
        'GET /api',
        'GET /api/rooms',
        # for a specific room this will be
        # used
        'GET /api/rooms/:id'
    ]

    # returning the json response
    # basically safe means we can use more than
    # just python dictionaries inside of this response
    return Response(routes)


@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    # as there are many objects which is 
    # going to be serialized
    serializer = RoomSerializer(rooms, many=True)
    # not returning the object but rather the data
    return Response(serializer.data)