import datetime

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"student/home.html")

def about(request):
    return render(request,"student/about.html")

def dashboard(request):
    return render(request,"student/dashboard.html")

def greetings(request,name):
    no1=2
    no2=3

    return render(request,"student/greetings.html",
                  {"username":name                                                                                                                                                                              ,"values":{"no1":no1,"no2":no2,"total":no1+no2}})

def isNewyear(request):
    date=datetime.datetime.utcnow()
    return render(request,"student/newyear.html",{
        "newyear":date.month==1 and date.day==1
    })
