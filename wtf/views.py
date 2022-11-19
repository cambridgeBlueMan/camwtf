from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("Home page for wtf app!!!!")
# Create your views here.
