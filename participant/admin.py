from django.contrib import admin
from team.models import Participant
from team.models import Team
from simple_history.admin import SimpleHistoryAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class ParticipantAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    list_display = (
        'id',
        'firstName',
        'lastName',
        'mobileNo',
        'emailID',
        'year',
        'college',
        '__team__')
    list_filter = (
        'id',
        'firstName',
        'lastName',
        'mobileNo',
        'emailID',)

admin.site.register(Participant, ParticipantAdmin)
