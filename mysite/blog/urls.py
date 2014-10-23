from django.conf.urls import patterns, include, url
from django.contrib import admin

from blog import views
urlpatterns = patterns('',
    url(r'^$', views.blog_list, name='index'),
    # url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    # url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)