from django.urls import path
from .views import main

urlpatterns = [
    path('home', main), #api/home
    path('', main) #api/
]