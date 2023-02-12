from django.contrib import admin
from django.urls import path, include

admin.site.site_header  =  "Admin Panel - Advaita IIIT-BH"  
admin.site.site_title  =  "Advaita IIIT-BH"
admin.site.index_title  =  "Advaita IIIT-BH"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]
