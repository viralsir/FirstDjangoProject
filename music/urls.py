from django.urls import path

import music
from .views import *
urlpatterns = [
    path('home/', home, name='home-page'),
    path('song/<int:songs_id>/', info, name='music-page'),
]