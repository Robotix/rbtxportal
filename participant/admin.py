from django.contrib import admin
from team.models import Participant
from team.models import Team
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.

class ParticipantAdmin(SimpleHistoryAdmin):
    list_display = (
        'id',
        'firstName',
        'lastName',
        'mobileNo',
        'emailID',
        'year',
        'college')
    list_filter = (
        'id',
        'firstName',
        'lastName',
        'mobileNo',
        'emailID',)

admin.site.register(Participant, ParticipantAdmin)
