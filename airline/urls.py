from django.urls import path
from .views import *
urlpatterns = [
    path('list/', listofairports, name='view-airport'),
]