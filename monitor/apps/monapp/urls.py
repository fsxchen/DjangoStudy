from django.conf.urls import patterns, url
from apps.monapp import views
#
#urlpatterns = patterns(views,
#    # Examples:
#    # url(r'^$', 'django_blog.views.home', name='home'),
#    url(r'^hello/', views.hello),
#    url(r'^index$', views.index),
#    url(r'^$', views.index),
#    url(r'^(?P<blog_id>\d+)/(?P<blog_link>\w*)$', views.blog_detail),
#)

urlpatterns = patterns('apps.monapp.views',

    #url(r'^index$', 'index', name='index'),
    url(r'^(?P<host_id>\d+)$', 'host_detail', name='host_detail'),
)
