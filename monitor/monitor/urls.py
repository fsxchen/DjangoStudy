from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'apps.monapp.views.index'),
    url(r'^host/', include('apps.monapp.urls', namespace='host')),
)
