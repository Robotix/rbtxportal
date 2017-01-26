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
            ('bombdisposal', 'Bomb Disposal'),
            ('conquest', 'Conquest'),
            ('bricks', 'B.R.I.C.K.S'),
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
        return '{}, {}'.format(participant.college.name, participant.college.city)


@admin.register(Participant)
class ParticipantAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = ParticipantResource
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
    inlines = [
        TeamInlineFactory(BombDisposal),
        TeamInlineFactory(Conquest),
        TeamInlineFactory(Bricks),
    ]
