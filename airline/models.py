from django.db import models

#makemigration : check model changes
#migrate  : apply all the changes.

# Create your models here.
class airport(models.Model):
    city = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.city + " - " + self.code


