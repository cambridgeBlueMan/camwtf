from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Region, Ig, Group, Venue, Meeting, Town

def main(request):
    meetings = Meeting.objects.all()
    template = loader.get_template('home/main.html')
    context = {
        'meetings': meetings
    }
    return HttpResponse(template.render(context, request))

def cambs(request):
    meetings = Meeting.objects.filter(venue__town__county = 5).order_by('venue__town__name','day')
    towns = Town.objects.filter(county = 5)
    template = loader.get_template('home/cambs.html')
    context = {
        'meetings': meetings,
        'towns': towns
    }
    return HttpResponse(template.render(context, request))

def ajax(request):
    meetings = Meeting.objects.all()
    template = loader.get_template('home/ajax.html')
    context = {
        'meetings': meetings
    }
    return HttpResponse(template.render(context, request))



def bs4(request):
    meetings = Meeting.objects.all()
    template = loader.get_template('home/bs4.html')
    context = {
        'meetings': meetings
    }
    return HttpResponse(template.render(context, request))

def intergroup(request, ig):
    """
    Takes an integer representing an intergroup and filters meetings based on
    that intergroup
    """
    meetings = Meeting.objects.filter(group__ig = ig).order_by('town','day')
    template = loader.get_template('home/main.html')
    context = {
        'meetings': meetings,
    }
    return HttpResponse(template.render(context, request))

def town(request, town):

    """ takes either an integer representing a town or string of the town name 
    and returns all meetings in that town """

    if type(town) is str:
        if town == 'all':
            meetings = Meeting.objects.all()
        else:    
            meetings = Meeting.objects.filter(venue__town__name = town)
    if type(town) is int:
        meetings = Meeting.objects.filter(venue__town__id = town)

    template = loader.get_template('home/by_town.html')
    context = {
        'meetings': meetings
    }
    return HttpResponse(template.render(context, request))

def byDay(request, ig):
    meetings = Meeting.objects.filter(group__ig = ig).order_by('day')
    town = Town.objects.filter(county = 15)
    #print(meetings)
    # initialise a list to hold lists for each days meetings
    sortedMeetings = [[],[],[],[],[],[],[]]
    # for i in range(7):
    #     # initialise inner lists to hold the data by day
    #     sortedMeetings[i]=[]
    # print(sortedMeetings)
    for meeting in meetings:
        for num in range(7):
            if meeting.day == num + 1:
                sortedMeetings[num].append(meeting)
    #print(sortedMeetings)
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    template = loader.get_template('home/by_day.html')
    context = {
        'meetings': meetings,
        'sortedMeetings': sortedMeetings,
        'days': days,
        'towns': town
    }
    return HttpResponse(template.render(context, request))

def ajaxByDay(request, ig):
    # add a filter for town
    meetings = Meeting.objects.filter(group__ig = ig).order_by('day')
    town = Town.objects.filter(county = 15)
    #print(meetings)
    # initialise a list to hold lists for each days meetings
    sortedMeetings = [[],[],[],[],[],[],[]]
    # for i in range(7):
    #     # initialise inner lists to hold the data by day
    #     sortedMeetings[i]=[]
    # print(sortedMeetings)
    for meeting in meetings:
        for num in range(7):
            if meeting.day == num + 1:
                sortedMeetings[num].append(meeting)
    #print(sortedMeetings)
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    template = loader.get_template('home/ajaxByDay.html')
    context = {
        'meetings': meetings,
        'sortedMeetings': sortedMeetings,
        'days': days,
        'towns': town
    }
    return HttpResponse(template.render(context, request))



