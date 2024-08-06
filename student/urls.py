from django.urls import path
from .views import *

urlpatterns = [
        path("home/",home,name="student-home"),
        path("aboutus/",about,name="student-about"),
        path("dashboard/",dashboard,name="student-dashboard"),
        path("greetings/<str:name>",greetings,name="student-greetings"),
        path("newyear/",isNewyear,name="student-newyear"),
]