__author__ = 'pmccloud'
from rest_framework.serializers import ModelSerializer
from foodrunner.core.models import Donation, Recipient


class DonationSerializer(ModelSerializer):
    class Meta:
        model = Donation


class RecipientSerializer(ModelSerializer):
    class Meta:
        model = Recipient
