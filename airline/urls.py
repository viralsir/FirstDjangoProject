from django.urls import path
from .views import *
urlpatterns = [
    path('list/', listofairports, name='view-airport'),
    path("flights/",flight_home,name="home-flight"),
    path("flights/<int:flight_id>",flight_details,name="flight-details"),
    # flights/1  fliths/2
]