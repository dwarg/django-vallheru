# -*- encoding: utf-8 -*-

from django.conf.urls import url

from .views import StatisticView, RaceView, ChosenRaceView

urlpatterns = [
    url(r'^statistic$', StatisticView.as_view(), name='statistic'),
    url(r'race/$', RaceView.as_view(), name='race'),
    url(r'race/(?P<pk>[0-9]+)/$', ChosenRaceView.as_view(), name='race_accept'),
]
