from django.db import models

DAY_CHOICES = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday')
]

COUNTRY_CHOICES = [
    ('England', 'England'),
    ('Scotland', 'Scotland'),
    ('Wales', 'Wales'),
    ('Northern Ireland', 'Northern Ireland')
]
# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Ig(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Group(models.Model):
    """
    """
    name = models.CharField(max_length=250)
    ig = models.ForeignKey(Ig, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class County(models.Model):
    """
    """
    name = models.CharField(max_length=100)
    country = models.CharField(max_length = 20,  default = 'England', choices = COUNTRY_CHOICES)

    def __str__(self):
        return self.name

class Town(models.Model):
    """
    """
    name = models.CharField(max_length=100)
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    description = models.TextField(blank = True)
    latitude=models.FloatField(null=True, blank=True)
    longtitude=models.FloatField(null=True, blank=True)

    """    
    null=True sets NULL (versus NOT NULL) on the column in your DB. Blank values for Django 
    field types such as DateTimeField or ForeignKey will be stored as NULL in the DB.

    blank determines whether the field will be required in forms. This includes the admin 
    and your custom forms. If blank=True then the field will not be required, whereas if it's 
    False the field cannot be blank.

    The combo of the two is so frequent because typically if you're going to allow a field 
    to be blank in your form, you're going to also need your database to allow NULL values for 
    that field. The exception is CharFields and TextFields, which in Django are never saved as 
    NULL. Blank values are stored in the DB as an empty string ('').
    """
    def __str__(self):
        return self.name

class Venue(models.Model):
    """
    """
    town=models.ForeignKey(Town, on_delete=models.PROTECT, blank=True)
    name=models.CharField(max_length=250)
    address1=models.CharField(max_length=250)
    address2=models.CharField(max_length=250, blank=True)
    address3=models.CharField(max_length=250, blank=True)
    postcode=models.CharField(max_length=10)
    latitude=models.FloatField(null=True)
    longtitude=models.FloatField(null=True)
    disabledAccess=models.BooleanField()
    description=models.TextField(blank=True)

    def __str__(self):
        return self.name

class Meeting(models.Model):
    """
    """
    class Day(models.IntegerChoices):
        SUN = 1, "Sunday"
        MON = 2, "Monday"
        TUE = 3, "Tuesday"
        WED = 4, "Wednesday"
        THU = 5, "Thursday"
        FRI = 6, "Friday"
        SAT = 7, "Saturday"

    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    day= models.IntegerField(choices = Day.choices, default = Day.SUN)
    startTime=models.TimeField()
    duration=models.DurationField()
    description= models.TextField(blank=True)

    def __str__(self):
        return f"{self.group}, {self.day}"
        #return self.group + self.day
