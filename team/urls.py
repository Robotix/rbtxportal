from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^register', 'team.views.register', name='register'),
    url(r'^find', 'team.views.find', name='find'),
    url(r'^search', 'team.views.search', name='search'),
	url(r'^status/(?P<id>\d+)', 'team.views.status', name='status'),
)
