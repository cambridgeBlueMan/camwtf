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

class Venue(models.Model):
    """
    """
    name=models.CharField(max_length=250)
    address1=models.CharField(max_length=250)
    address2=models.CharField(max_length=250, blank=True)
    postcode=models.CharField(max_length=10)
    lattitude=models.FloatField()
    longitude=models.FloatField()
    disabledAccess=models.BooleanField()
    description=models.TextField(blank=True)

    def __str__(self):
        return self.name

class Meeting(models.Model):
    """
    """
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    startTime=models.TimeField()
    duration=models.DurationField()
    description= models.TextField()

    def __str__(self):
        return f"{self.group}, {self.day}"
        #return self.group + self.day
