from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    # def __str__(self):
    #     return self.save
    lat = models.FloatField()
    lng = models.FloatField()

class PickupRequest(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    status = models.CharField(max_length=20, default='pending') 