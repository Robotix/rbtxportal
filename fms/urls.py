from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'fms.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^team/', include('team.urls')),
)
