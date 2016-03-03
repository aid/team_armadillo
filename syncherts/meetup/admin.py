from django.contrib import admin

# Register your models here.

from .models import Location, Sponsor, Meeting

admin.site.register(Location)
admin.site.register(Sponsor)
admin.site.register(Meeting)
