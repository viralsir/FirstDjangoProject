from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello World!</h1>')

def about(request):
    return HttpResponse('<h1>About us</h1>')

def contact(request):
    return HttpResponse('<h1>Contact us</h1>')

def dashboard(request):
    return HttpResponse('<h1>Dashboard</h1>')