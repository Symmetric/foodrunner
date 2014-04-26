from django.forms import ModelForm
from django.forms.widgets import HiddenInput
from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework.viewsets import ModelViewSet
from foodrunner.core.models import Donation, Recipient
from rest_framework import generics
from foodrunner.core.serializers import DonationSerializer, RecipientSerializer
from rest_framework import permissions


class DonationForm(ModelForm):
    class Meta:
        model = Donation
        widgets = {
            'location_lat': HiddenInput,
            'location_lng': HiddenInput
        }


class DonationViewset(ModelViewSet):
    """
    REST API view for Donation model.
    """
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer


class RecipientViewset(ModelViewSet):
    """
    REST API view for Recipient model.
    """
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer


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


def pickup(request):
    return render_to_response(
        'pickup.html',
        {},
        context_instance=RequestContext(request),
    )
