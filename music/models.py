from django.db import models

# Create your models here.
class songs(models.Model):
    song_name = models.CharField(max_length=50)
    song_code=models.IntegerField()

    def __str__(self):
        return self.song_name

class singers(models.Model):
    singer_Id = models.ManyToManyField(songs,related_name='singer')
    singer_name = models.CharField(max_length=10)
    singer_address = models.CharField(max_length=50)

    def __str__(self):
        return self.singer_name