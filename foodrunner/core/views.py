from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    return render_to_response(
        'index.html',
        {},
        context_instance=RequestContext(request),
    )


def donate(request):
    return render_to_response(
        'donate.html',
        {},
        context_instance=RequestContext(request),
    )


def pickup(request):
    return render_to_response(
        'pickup.html',
        {},
        context_instance=RequestContext(request),
    )
