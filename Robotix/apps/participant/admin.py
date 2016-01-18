from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Participant


@admin.register(Participant)
class ParticipantAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (('first_name', 'last_name'),),
            'classes': ('wide',),
        }),
        ('Contact Information', {
            'fields': (('mobile', 'email'),),
            'classes': ('wide',),
        }),
        ('Academic Information', {
            'fields': ('year', 'college'),
            'classes': ('wide',),
        }),
    )
    list_filter = [
        'college__name',
        'college__state',
        'year',
    ]
    list_display = [
        'name',
        'email',
        'mobile',
    ]
    search_fields = [
        '=first_name',
        '=last_name',
        'email',
        'mobile',
    ]
