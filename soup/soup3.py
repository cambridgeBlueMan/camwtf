# to run this from django shell

# >>> exec(open('soup/soup3.py').read())
import datetime
# import the models
from wtf.models import Region, Ig, Group, Venue, Meeting

# get the Ig 
ig = Ig.objects.get(pk=1)

	# add the group and save it in g
g = Group(name = "twattox", ig = ig)
g.save()

# add the venue and saave it in v
v = Venue(
    name = "twattox hattox",
    address1 = "addressingtons" ,
    address2 = "thadessingtons",
    address3 = "spritas",
    postcode = "CB1 3TN",
    twattock = "",
    latitude = float(1.22345), #latitude[ix],
    longtitude = float(9.66666), #longtitude[ix],
    disabledAccess = True
)
v.save()
# now you can add the meeting
m = Meeting(
    group = g,
    venue = v,
    day = "Thursday",
    startTime = datetime(now),
    duration = duration(hour = 1),
    description = ""
)
m.save()