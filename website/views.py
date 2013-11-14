from django.http import Http404
from django.shortcuts import render_to_response
from website.models import *

def index(request):
    return render_to_response('status/index.html', {'pages': StatusPage.objects.all()})

def page(request, pk):
    page = None
    try:
        page = StatusPage.objects.get(pk=pk)
    except StatusPage.DoesNotExist:
        raise Http404
    services = Service.objects.filter(page=page)
    return render_to_response('status/status.html', {'page': page,'services':services})