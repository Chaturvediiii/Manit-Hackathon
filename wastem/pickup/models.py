from django.db import models



class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.name


CHOICES = [('R', 'recyclable'), ('NR', 'non-recyclable'), ('both', 'both')]


class PickupRequest(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    type = models.CharField(choices=CHOICES, max_length=25,
                            default=None, null=True, blank=False)
    description = models.CharField(max_length=200, default='none')
    phone_number = models.CharField(max_length=20, default='+91')
    # pending,approved,rejected,cancelled
    status = models.CharField(max_length=12, default='pending')
    
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.status
