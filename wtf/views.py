from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Region, Ig, Group, Venue, Meeting

def main(request):
    meetings = Meeting.objects.all()
    template = loader.get_template('home/main.html')
    context = {
        'meetings': meetings
    }
    return HttpResponse(template.render(context, request))

def intergroup(request, ig):
    """
    Takes an integer representing an intergroup and filters meetings based on
    that intergroup
    """
    meetings = Meeting.objects.filter(group__ig = ig)
    template = loader.get_template('home/main.html')
    context = {
        'meetings': meetings
    }
    return HttpResponse(template.render(context, request))

def town(request, town):
    """ takes either an integer representing a town or string of the town name 
    and returns all meetings in that town """
    
    if type(town) is str:
        meetings = Meeting.objects.filter(venue__town__name = town)
    
    if type(town) is int:
        meetings = Meeting.objects.filter(venue__town__id = town)
    
    template = loader.get_template('home/main.html')
    context = {
        'meetings': meetings
    }
    return HttpResponse(template.render(context, request))


