from django.contrib import admin

# Register your models here.

from .models import Pizza, Poll, Tally, Vote

admin.site.register(Pizza)
admin.site.register(Poll)
admin.site.register(Tally)
admin.site.register(Vote)

