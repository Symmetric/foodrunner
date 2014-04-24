__author__ = 'pmccloud'
from rest_framework.serializers import ModelSerializer
from foodrunner.core.models import Donation


class DonationSerializer(ModelSerializer):
    class Meta:
        model = Donation
