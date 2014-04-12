__author__ = 'pmccloud'

from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from foodrunner.core import views

urlpatterns = patterns(
    'foodrunner.core.views',
    url(r'^$', views.index, name='index'),
    url(r'^donations/$', views.DonationList.as_view()),
    url(r'^donations/(?P<pk>[0-9]+)/$', views.DonationDetail.as_view()),

)

urlpatterns = format_suffix_patterns(urlpatterns)