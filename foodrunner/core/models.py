from django.db import models


class Donation(models.Model):
    """A donation that a user has anounced is available for pickup."""
    location_lat = models.FloatField()
    location_lng = models.FloatField()
    weight = models.IntegerField()
    description = models.CharField(max_length=1000)
    contact_number = models.CharField(max_length=1000)
    available_time = models.CharField(max_length=1000)
    expire_time = models.CharField(max_length=1000)

    # provider = models.ForeignKey('Provider')


# class Provider(models.Model):
#
#     primary_name = models.CharField(max_length=300)
#     primary_number = models.CharField(max_length=12)
#     primary_email = models.EmailField(max_length=100)
#     address = models.CharField(max_length=300)
#
#
#     #For secondary contact, not required
#     secondary_name = models.CharField(max_length=300,blank=True)
#     secondary_number = models.CharField(max_length=12,blank=True)
#     secondary_email = models.EmailField(max_length=100,blank=True)


