from django.db import models

# Create your models here.

class Donation(models.Model):

    location = models.CharField(max_length=1000)

    # VOLUME_CHOICES = (
    #     ('SMALL', 1),
    #     ('MEDIUM', 2),
    #     ('LARGE', 3),
    #     ('EXTRA LARGE', 4)
    # )
    weight = models.IntegerField()
    description = models.CharField(max_length=1000)
    contact_number = models.CharField(max_length=1000)
    # provider = models.ForeignKey('Provider')
    available_time = models.CharField(max_length=1000)
    expire_time = models.CharField(max_length=1000)


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


