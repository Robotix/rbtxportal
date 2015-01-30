from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^register', 'participant.views.register', name='register'),
    url(r'^find', 'participant.views.find', name='find'),
    url(r'^status/(?P<id>\d+)', 'participant.views.status', name='status'),
)
