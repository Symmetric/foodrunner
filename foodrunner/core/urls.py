from django.conf.urls import url, patterns, include
from rest_framework import routers
from foodrunner.core import views
from foodrunner.core.views import RecipientViewset, DonationViewset

router = routers.DefaultRouter()
router.register('donations', DonationViewset)
router.register('recipients', RecipientViewset)

urlpatterns = patterns(
    'foodrunner.core.views',
    url(r'^$', views.index, name='index'),
    url(r'^donate$', views.donate, name='donate'),
    url(r'^pickup$', views.pickup, name='pickup'),

    # REST API
    url(r'^api/', include(router.urls))
)
