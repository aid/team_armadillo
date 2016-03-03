
from rest_framework import serializers
from pizza.models import Pizza, Poll, Tally, Vote

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('id', 'name', 'vegetarian', 'ingredients', 'calories', 'thumbnail_url')

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('id', 'meeting', 'voting_close')

class TallySerializer(serializers.ModelSerializer):
    class Meta:
        model = Tally
        fields = ('id', 'poll', 'pizza', 'voting_count')

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('id', 'attendee_email', 'attendee_vegetarian', 'poll', 'pizza')

