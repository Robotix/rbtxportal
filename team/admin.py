from django.contrib import admin
from team.models import Team
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.

class TeamAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'event', 'certificate_given', )
    list_filter = ['id', 'event', 'certificate_given']

admin.site.register(Team, TeamAdmin)
