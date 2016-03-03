from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    postcode = models.CharField(max_length=15)

    def __str__(self):
            return self.name

class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    logo_url = models.URLField()
    logo = models.ImageField(upload_to='images')

    def __str__(self):
            return self.name

class Meeting(models.Model):
    start = models.DateTimeField(max_length=200)
    location = models.ForeignKey(Location)
    sponsor = models.ForeignKey(Sponsor)

    def __str__(self):
            return "Meeting at {t} at {l} sponsored by {s}".format(
                t=self.start,
                l=self.location,
                s=self.sponsor)


        

