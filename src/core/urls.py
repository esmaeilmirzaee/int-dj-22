from django.contrib import admin
from django.urls import path

from django.urls import include

urlpatterns = [
    path('', include('demo.urls', namespace='demo')),
    path('admin/', admin.site.urls),
]
