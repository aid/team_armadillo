
from django.conf.urls import url
from pizza import views


urlpatterns = [
    url(r'^pizzas/$', views.PizzaList.as_view()),
    url(r'^pizzas/(?P<pk>[0-9]+)/$', views.PizzaDetail.as_view()),

    url(r'^polls/$', views.PollList.as_view()),
    url(r'^polls/(?P<pk>[0-9]+)/$', views.PollDetail.as_view()),

    url(r'^tallys/$', views.TallyList.as_view()),
    url(r'^tallys/(?P<pk>[0-9]+)/$', views.TallyDetail.as_view()),

    url(r'^votes/$', views.VoteList.as_view()),
    url(r'^votes/(?P<pk>[0-9]+)/$', views.VoteDetail.as_view()),
]

