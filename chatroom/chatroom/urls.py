from django.contrib import admin
from django.urls import path, include # inlcude is imported 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')), # Here base app is included all the urlpatterns 
                                  # from base is found here

    path('api/', include('base.api.urls'))
]

# concatenating the url 
# basically by all this the image is going to get the url 
# of images/ 
# and get stored in the selected folder
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
