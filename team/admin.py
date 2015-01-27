from django.contrib import admin
from team.models import Team
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.

class TeamAdmin(SimpleHistoryAdmin):
    list_display = ('__unicode__', 'event', 'number', 'certificate_given', 'verified' )
    list_filter = ['event', 'certificate_given', 'verified']

admin.site.register(Team, TeamAdmin)
