from django.conf.urls.defaults import *
from eventmanager.views import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
         (r'^$', root),
         (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
         (r'^admin/', include(admin.site.urls)),
         (r'^basicinfo/(.*)', retrieve_basic_team_information),
         (r'^bestalgo/', best_algorithm_design),
         (r'^bestmech/', best_mechanical_design),
         (r'^estimate_score/([a-zA-Z][a-zA-Z])/([0-9])/', estimate_score),
         (r'^info/(.*)', retrieve_team_information),
         (r'^judge/([a-zA-Z][a-zA-Z])/([0-9])/([a-zA-Z][a-zA-Z][0-9]+)', master_judge),
         (r'^list/(.*)', retrieve_list_of_registered_teams),              
         (r'^logout/$', logout),
         (r'^notscored/([a-zA-Z][a-zA-Z])/([0-9])/', teams_not_scored),
         (r'^promote/([a-zA-Z][a-zA-Z])/([0-9])/', promotion_interface),
         (r'^register/', register_team),
         (r'^scores/([a-zA-Z][a-zA-Z])/([0-9])/', score_board),
         (r'^nuketimer/', nuke_timer)
)
