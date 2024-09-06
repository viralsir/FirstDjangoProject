from django.shortcuts import render
from .models import singers,songs
# Create your views here.

def home(request):
    git=songs.objects.all()
    return render(request,"studio/songs.html",{"git":git})

def info(request,songs_id):
    song=songs.objects.get(pk=songs_id)

    return render(request,"studio/singers.html",
                  {
                      "song":song,
                      "singer":song.singer.all()
                   })