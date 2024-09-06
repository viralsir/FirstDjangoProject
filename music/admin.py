from django.contrib import admin
from .models import singers,songs
# Register your models here.
admin.site.register(songs)
admin.site.register(singers)