from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Region, Ig, Group, Venue, Meeting, Town
from math import radians, cos, sin, asin, sqrt

def cambs(request):
    meetings = Meeting.objects.filter(venue__town__county = 5).order_by('venue__town__name','day')
    towns = Town.objects.filter(county = 5)
    template = loader.get_template('home/base_template.html')
    context = {
        'meetings': meetings,
        'towns': towns
    }
    return HttpResponse(template.render(context, request))

def byTown(request, theTown, lnRange):
    if theTown == 1722:
        meetings = Meeting.objects.filter(venue__town__county = 5) #.order_by('venue_town')
    else:
        meetings = list(Meeting.objects.filter(venue__town__id = theTown).order_by('day'))
        # get the town, so we can access the lat and long
        center = Town.objects.filter(id = theTown)
        if lnRange > 0:
            # get all meetings and add those within the current lnRange
            allMeetings = Meeting.objects.filter(venue__town__county = 5).order_by('day')
            # test these meetings for distance from center and 
            # if appropriate add to the dataset
            for meeting in allMeetings:
                if calcDistance(
                    center[0].latitude,
                    center[0].longtitude,
                    meeting.venue.latitude,
                    meeting.venue.longtitude,
                    lnRange
                    ) == True:
                    # need to check whether we already got it and then we need to sort
                    meetings.append(meeting)
            
            meetings = list(dict.fromkeys(meetings))
            #meetings.sort(key=center[0].name)


    towns = Town.objects.filter(county = 5)
    template = loader.get_template('home/byTown.html')
    context = {
        'meetings': meetings,
        'towns': towns

    }
    return HttpResponse(template.render(context, request))

def byDay(request, theTown, lnRange):
    # get list of towns for this county to populate dropdown
    # if this is for all towns
    if theTown == 1722:
        # get query set of all meetings
        meetings = Meeting.objects.filter(venue__town__county = 5).order_by('day')
    else:
        # get query set for the specified town 
        meetings = list(Meeting.objects.filter(venue__town__id = theTown).order_by('day'))

        # get the town, so we can subsequently access its lat and long
        center = Town.objects.filter(id = theTown)

        if lnRange > 0:
            # get all meetings and add those within the current lnRange
            allMeetings = Meeting.objects.filter(venue__town__county = 5).order_by('day')
            # test these meetings for distance from center and 
            # if appropriate add to the dataset
            for meeting in allMeetings:
                if calcDistance(
                    center[0].latitude,
                    center[0].longtitude,
                    meeting.venue.latitude,
                    meeting.venue.longtitude,
                    lnRange
                    ) == True:
                    # need to check whether we already got it and then we need to sort
                    meetings.append(meeting)
            
            meetings = list(dict.fromkeys(meetings))
            #meetings.sort(key=center[0].name)
    # initialise a list to hold lists for each days meetings
    sortedMeetings = [[],[],[],[],[],[],[]]
    for meeting in meetings:
        for i in range(7):
            if meeting.day == i + 1:
                sortedMeetings[i].append(meeting)
    # if there are no meetings for a particular day then the list element will be empty
    sortedMeetings = [x for x in sortedMeetings if x]
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    template = loader.get_template('home/byDay.html')
    towns = Town.objects.filter(county = 5)
    context = {
        'meetings': meetings,
        'sortedMeetings': sortedMeetings,
        'days': days,
        'towns': towns
    }
    return HttpResponse(template.render(context, request))


def calcDistance(lat1, lon1, lat2, lon2, distance ):
     
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
      
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
    c = 2 * asin(sqrt(a))
    
    # Radius of earth in kilometers. Use 3956 for miles
    r = 3956
      
    # calculate the result
    if (c * r) <= distance:
        lnret =  True
    else:
        lnret =  False
    print("distance is: ", (c*r), lnret)
    return lnret
