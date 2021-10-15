from django.urls import path
from .views import home,room


# Create urlspatterns

urlpatterns = [
    path('', home, name='home'),
    path('room/', room , name='room')
]