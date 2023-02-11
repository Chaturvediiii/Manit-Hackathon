from django.db import models
from django.contrib.postgres.fields import ArrayField

class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.name


class PickupRequest(models.Model):
    CHOICES = [('R','recyclable'),('NR','non-recyclable'),('none','none')]
    choices = ArrayField(
        models.CharField(choices=CHOICES, max_length=4, blank=True, default='none'),
    )
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    # type = models.OneToOneField(to, on_delete)(max_length=4,choices= CHOICES)
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return self.status