from django.conf.urls import patterns, include, url

from django.contrib import admin



admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('foodrunner.core.urls')),

)
# This is to add a login option for the API
# This can eventually be used to make sure that only the right
# people have access to the API
urlpatterns += patterns(
    '',

    url(r'^api-auth/', include('rest_framework.urls',
                                namespace='rest_framework'))
)
