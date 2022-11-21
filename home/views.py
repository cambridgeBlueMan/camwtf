from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def tags(request):
    template = loader.get_template('home/main.html')
    context = {'aTag': 'Leas first tag'
    }
    return HttpResponse(template.render(context, request))

