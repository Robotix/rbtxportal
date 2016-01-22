from django.contrib import admin

from import_export.admin import ExportMixin
from jet.filters import RelatedFieldAjaxListFilter

from .models import Participant


class TeamListFilter(admin.SimpleListFilter):
    title = 'Team'
    parameter_name = 'team'

    def lookups(self, request, model_admin):
        return (
            ('droidblitz', 'Droid Blitz'), 
            ('summit', 'Summit'),
            ('sherlock', 'Sherlock'),
            ('sheldon', 'S.H.E.L.D.O.N.'),
            ('warehouse', 'Warehouse'),
        )

    def queryset(self, request, queryset):
        if self.value():
            query = dict()
            query['team_{}_related__isnull'.format(self.value())] = False
            return queryset.filter(**query)
        return queryset


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
        TeamListFilter,
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
