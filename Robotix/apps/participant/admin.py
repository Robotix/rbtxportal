from django.contrib import admin

from import_export.admin import ExportMixin
from jet.filters import RelatedFieldAjaxListFilter

from .models import Participant


@admin.register(Participant)
class ParticipantAdmin(ExportMixin, admin.ModelAdmin):
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
        ('college', RelatedFieldAjaxListFilter),
        'college__state',
        'year',
    ]
    list_display = [
        'name',
        'email',
        'mobile',
        'college',
    ]
    search_fields = [
        '=first_name',
        '=last_name',
        'email',
        'mobile',
    ]
