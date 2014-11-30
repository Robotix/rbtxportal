from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<event>\d{3})/(?P<id>\d{3})/$',views.status, name= 'status'),
    url(r'^submit/$', views.submit, name= 'submit'),
 )