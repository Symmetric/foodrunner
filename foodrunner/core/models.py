from django.db import models

# Create your models here.

class Pickup(models.Model):

    location = models.CharField()

    VOLUME_CHOICES = (
        ('SMALL', 1),
        ('MEDIUM', 2),
        ('LARGE', 3),
        ('EXTRA LARGE', 4)
    )
    volume = models.IntegerField(choices=VOLUME_CHOICES, default='SMALL')

    provider = models.ForeignKey('Provider')
    available_time = models.DateTimeField
    expire_time = models.DateTimeField

class Provider(models.Model):

    primary_name = models.CharField()
    primary_number = models.CharField()
    primary_email = models.EmailField()
    address = models.CharField()


    #For secondary contact, not required
    secondary_name = models.CharField(blank=True)
    secondary_number = models.Charfield(blank=True)
    secondary_email = models.EmailField(blank=True)


