from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Hey this is change txt"
admin.site.site_title = "icoder Admin Panel"
admin.site.index_title = "Welcome to icoder Admin Panel"




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ux.urls')),
]
