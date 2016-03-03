
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from meetup import views

urlpatterns = [
    url(r'^locations/$', views.LocationList.as_view()),
    url(r'^locations/(?P<pk>[0-9]+)/$', views.LocationDetail.as_view()),
    
    url(r'^sponsors/$', views.SponsorList.as_view()),
    url(r'^sponsors/(?P<pk>[0-9]+)/$', views.SponsorDetail.as_view()),

    url(r'^meetings/$', views.MeetingList.as_view()),
    url(r'^meetings/(?P<pk>[0-9]+)/$', views.MeetingDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
