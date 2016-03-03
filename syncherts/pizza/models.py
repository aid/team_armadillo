from django.db import models

from meetup.models import Meeting

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    vegetarian = models.BooleanField()
    ingredients = models.CharField(max_length=500)
    calories = models.IntegerField()
    thumbnail_url = models.URLField()
    thumbnail = models.ImageField(upload_to="images")
    
    def __str__(self):
            return self.name


class Poll(models.Model):
    meeting = models.ForeignKey(Meeting)
    voting_close = models.DateTimeField()

    def __str__(self):
            return "Poll for meeting {m} closing at {t}".format(
                m=meeting,
                t=voting_close)

class Tally(models.Model):
    poll = models.ForeignKey(Poll)
    pizza = models.ForeignKey(Pizza)
    voting_count = models.IntegerField(default=0)
    

    def __str__(self):
            return "Poll for meeting {m} closing at {t}".format(
                m=meeting,
                t=voting_close)

class Vote(models.Model):
    attendee_email = models.EmailField()
    attendee_vegetarian = models.BooleanField()
    poll = models.ForeignKey(Poll)
    pizza = models.ForeignKey(Pizza)

    def __str__(self):
            return "Vote by {a} {v} on poll {p} for pizza {z}".format(
                a=self.attendee_email,
                v='- a vegitarian -' if self.attendee_vegetarian else '- not a vegitarian -',
                p=self.poll,
                z=self.pizza)

