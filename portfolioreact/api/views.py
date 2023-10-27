from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Handle api endpoints.
# ie -> location on web server 
#   /home /profile 

def main(request):
    return HttpResponse('<h1>Testing<h1>')