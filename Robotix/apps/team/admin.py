from django.contrib import admin
from django import forms
from import_export.admin import ImportExportModelAdmin

from .models import *


class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = '__all__'

    def clean_participant(self):
        if len(self.cleaned_data['participant']) > self.Meta.model.max_team_size:
            raise forms.ValidationError(
                'Max team size is {}'.format(self.Meta.model.max_team_size),
                code='invalid'
            )


@admin.register(Summit)
@admin.register(Warehouse)
@admin.register(Sherlock)
@admin.register(Sheldon)
@admin.register(DroidBlitz)
class TeamAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = [
        '=participants__first_name',
        '=participants__last_name',
        'participants__email',
        'participants__mobile',
    ]
    form = TeamForm

    def get_fieldsets(self, request, obj=None, **kwargs):
        fieldsets = [
            (None, {
                'fields': ('participant',),
                'classes': ('wide',)
            }),
            ('Complete Postal Address', {
                'fields': (
                    ('street', 'locality'),
                    ('city', 'pin'),
                    ('state',),
                ),
                'classes': ('wide'),
            }),
            ('Scoring', {
                'fields': (
                    ('round_one', 'qualify_round_one',),
                    ('round_two', 'qualify_round_two',),
                    ('round_three',),
                ),
                'classes': ('wide'),
            }),
            ('Help Desk', {
                'fields': (
                    ('verification', 'certificate',),
                ),
                'classes': ('wide'),
            }),
        ]
        if not request.user.is_superuser:
            return fieldsets[:-2]
        return fieldsets

    def get_list_display(self, request, obj=None, **kwargs):
        list_display = [
            'round_one',
            'qualify_round_two',
            'round_two',
            'qualify_round_two',
            'round_three',
        ]
        if request.user.get_username() == 'helpdesk':
            return ['__str__', 'verification', 'certificate',] + list_display
        return ['__str__',] + list_display

    def get_list_filter(self, request, obj=None, **kwargs):
        list_filter = [
            'qualify_round_one',
            'qualify_round_two',
        ]
        if request.user.get_username() == 'helpdesk':
            return ['verification', 'certificate',] + list_filter
        return list_filter
