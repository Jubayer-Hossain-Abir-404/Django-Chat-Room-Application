from webbrowser import get
from django.http import JsonResponse

# This is going to be in views that
# shows all the routes in our APi
def getRoutes(request):
    # url or routes are gonna be two get
    # methods
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
    return JsonResponse(routes, safe=False)