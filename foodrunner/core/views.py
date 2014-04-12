from django.forms import ModelForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from foodrunner.core.models import Donation
from rest_framework import generics
from foodrunner.core.serializers import DonationSerializer
from rest_framework import permissions

class DonationForm(ModelForm):
    class Meta:
        model = Donation

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
    form = DonationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        form = DonationForm()
    return render_to_response(
        'index.html',
        {'form': form},
        context_instance=RequestContext(request),
    )

