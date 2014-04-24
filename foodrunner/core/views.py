from django.forms import ModelForm
from django.forms.widgets import HiddenInput
from django.shortcuts import render_to_response
from django.template import RequestContext
from foodrunner.core.models import Donation
from rest_framework import generics
from foodrunner.core.serializers import DonationSerializer
from rest_framework import permissions


class DonationForm(ModelForm):
    class Meta:
        model = Donation
        widgets = {
            'location_lat': HiddenInput,
            'location_lng': HiddenInput
        }


class DonationList(generics.ListCreateAPIView):
    """
    List all donations or create a new donation
    """
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer


class DonationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a donation
    """
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer


def index(request):
    return render_to_response(
        'index.html',
        {},
        context_instance=RequestContext(request),
    )


def donate(request):
    form = DonationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        form = DonationForm()
    return render_to_response(
        'donate.html',
        {'form': form},
        context_instance=RequestContext(request),
    )
