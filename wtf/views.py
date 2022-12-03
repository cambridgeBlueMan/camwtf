from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Region, Ig, Group, Venue, Meeting

def main(request):
    meetings = Meeting.objects.all()
    print(Meeting.objects.all)
    template = loader.get_template('home/main.html')
    context = {
        'aTag': meetings,
        'meetings': meetings

    }
    return HttpResponse(template.render(context, request))


