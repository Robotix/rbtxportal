from django.contrib import admin

from import_export.admin import ExportMixin
from import_export import resources
from jet.filters import RelatedFieldAjaxListFilter

from team.models import *
from team.admin import TeamInlineFactory

from .models import Participant


class TeamListFilter(admin.SimpleListFilter):
    title = 'Team'
    parameter_name = 'team'

    def lookups(self, request, model_admin):
        return (
            ('crusade', 'Crusade'),
            ('cubiscan', 'Cubiscan'),
            ('zenith', 'Zenith'),
        )

    def queryset(self, request, queryset):
        if self.value():
            query = dict()
            query['team_{}_related__isnull'.format(self.value())] = False
            return queryset.filter(**query)
        return queryset


class ParticipantResource(resources.ModelResource):

    class Meta:
        model = Participant
        use_transactions = True

    def dehydrate_college(self, participant):
        return participant.college.name


@admin.register(Participant)
class ParticipantAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = ParticipantResource
    fieldsets = (
        ('Contact Information', {
            'fields': (
		('first_name'),
		('last_name'),
		('mobile'),
		('email'),
                ('year'),
		('college'),
            ),
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
    inlines = [
        TeamInlineFactory(Crusade),
        TeamInlineFactory(Cubiscan),
        TeamInlineFactory(Zenith),
    ]
