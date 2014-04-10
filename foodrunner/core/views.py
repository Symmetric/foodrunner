from django.forms import ModelForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from foodrunner.core.models import Donation



class DonationForm(ModelForm):
    class Meta:
        model = Donation

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

