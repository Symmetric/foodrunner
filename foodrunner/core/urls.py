from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from foodrunner.core import views

urlpatterns = patterns(
    'foodrunner.core.views',
    url(r'^$', views.index, name='index'),
    url(r'^donate$', views.donate, name='donate'),
    url(r'^pickup$', views.pickup, name='pickup'),

    # REST API
    url(r'^api/donations/$', views.DonationList.as_view()),
    url(r'^api/donations/(?P<pk>[0-9]+)/$', views.DonationDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)