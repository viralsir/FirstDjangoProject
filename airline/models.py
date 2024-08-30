from django.db import models

#makemigration : check model changes
#migrate  : apply all the changes.

# Create your models here.
class airport(models.Model):
    city = models.CharField(max_length=100)
    code = models.CharField(max_length=100)


    def __str__(self):
        return self.city + " - " + self.code


class flight(models.Model):
    departure = models.ForeignKey(airport, on_delete=models.CASCADE, related_name='flight_departure')
    arrival = models.ForeignKey(airport, on_delete=models.CASCADE, related_name='flight_arrival')
    duration = models.IntegerField(default=0)
    def __str__(self):
        return self.departure.city + " -> " + self.arrival.city
