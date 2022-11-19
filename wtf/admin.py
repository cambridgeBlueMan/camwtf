from django.contrib import admin

# Register your models here.
from .models import Region, Ig, Group, Venue, Meeting
admin.site.register(Region)
admin.site.register(Ig)
admin.site.register(Group)
admin.site.register(Venue)
admin.site.register(Meeting)