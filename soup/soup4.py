from wtf.models import Region, Ig, Group, Venue, Meeting
v = Venue.objects.get(pk=0)
print(v.latitude)
