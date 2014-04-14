__author__ = 'pmccloud'
from rest_framework import serializers
from foodrunner.core.models import Donation

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ('location','weight','description','contact_number','available_time','expire_time')



    def restore_object(self, attrs, instance=None):
        """
        Create or update a new donation instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """

        if instance:
            #Update existing instance
            instance.location = attrs.get('location', instance.location)
            instance.weight = attrs.get('weight', instance.weight)
            instance.description = attrs.get('description', instance.description)
            instance.contact_number = attrs.get('contact_number', instance.contact_number)
            instance.available_time = attrs.get('available_time', instance.available_time)
            instance.expire_time = attrs.get('expire_time', instance.expire_time)
            return instance

        #Create new instance
        return Donation(**attrs)

