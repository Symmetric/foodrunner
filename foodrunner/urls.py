from django.conf.urls import patterns, include, url

from django.contrib import admin
from foodrunner.core import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^donate', views.donate, name='donate'),
    url(r'^pickup', views.pickup, name='pickup'),

    url(r'^admin/', include(admin.site.urls)),
)
