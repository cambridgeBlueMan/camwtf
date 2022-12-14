from django.contrib import admin

# Register your models here.
from .models import Region, Ig, Group, Venue, Meeting, Town, County
admin.site.register(Region)
admin.site.register(Ig)
admin.site.register(Group)
#admin.site.register(Venue)
admin.site.register(Meeting)
#admin.site.register(Town)
admin.site.register(County)

@admin.register(Town)
class TownAdmin(admin.ModelAdmin):
    list_display = ('name', 'county', 'description')
    search_fields = ('name',)
    list_filter = ('county',)
    ordering = ('county', 'name')

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name',)
    

