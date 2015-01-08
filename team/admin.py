from django.contrib import admin
from team.models import Team

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'event', 'certificate_given')
    list_filter = ['id', 'event', 'certificate_given']

admin.site.register(Team, TeamAdmin)
