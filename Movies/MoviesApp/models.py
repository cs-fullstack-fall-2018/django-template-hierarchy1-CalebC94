from django.db import models


class Movies(models.Model):
    name = models.CharField(max_length=100)
    yearReleased = models.IntegerField()
    ageAllowed = models.IntegerField()
    genres = models.CharField(max_length=100)

    def __str__(self):
        return  self.name