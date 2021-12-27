from django.contrib import admin
from django.urls import path, include # inlcude is imported 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')) # Here base app is included all the urlpatterns 
                                  # from base is found here
]
