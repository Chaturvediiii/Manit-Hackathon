from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.name


class PickupRequest(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    # CHOICES = [('R','recyclable'),('NR','non-recyclable'),('none','none')]
    # type = models.CharField(max_length=10,choices= CHOICES,default='none')
    description = models.CharField(max_length=200, default='none')
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return self.status