from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include("store.urls")),
     path('cart/', include("cart.urls")),
     
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 

admin.site.site_header = "BODMARLEY"
admin.site.site_title = "BODMARLEY"
admin.site.index_title = "bod marley"
