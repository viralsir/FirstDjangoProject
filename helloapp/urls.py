from django.urls import path
from .views import *

      #localhost :8080/hello/home
urlpatterns = [
    path('home/', home, name='home'),
    path("aboutus/",about,name="aboutus"),
    path("contact/",contact,name="contact"),
    path("dashboard/",dashboard,name="dashboard"),
]