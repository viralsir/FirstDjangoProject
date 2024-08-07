from django.urls import path
from .views import *

urlpatterns = [
     path('',home, name='task-home'),
     path('add/',addTask,name='task-add'),
]