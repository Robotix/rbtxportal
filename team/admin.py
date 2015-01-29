from django.contrib import admin
from django import forms
from team.models import Team
from simple_history.admin import SimpleHistoryAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from tekextensions.widgets import SelectWithPopUp
from cascade_round_one.models import Cascade_round_one
from cascade_round_two.models import Cascade_round_two

# Register your models here.

class TeamAdminForm(forms.ModelForm):
    cascade_round_one = forms.ModelChoiceField(Cascade_round_one.objects, widget=SelectWithPopUp)
    cascade_round_two = forms.ModelChoiceField(Cascade_round_two.objects, widget=SelectWithPopUp)
    class Meta:
        model = Team
        fields = '__all__'

class TeamResource(resources.ModelResource):

    class Meta:
        model = Team

class TeamAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    form = TeamAdminForm
    resource_class = TeamResource
    list_display = ('__unicode__', 'event', 'number', 'verified', 'qualify_round_one', 'qualify_round_two', 'certificate_given', '__participant_names__' )
    list_filter = ['event', 'certificate_given', 'verified', 'qualify_round_one', 'qualify_round_two']
    fieldsets = (
        ('Team Info', {
            'fields': ('event','number','participant_number','participant', 'certificate_given', 'verified')
        }),
        ('Address', {
            'classes': ('collapse',),
            'fields': ('street','locality','city','state','pin')
        }),
        ('Scoring', {
            'classes': ('collapse',),
            'fields': ('cascade_round_one','qualify_round_one', 'cascade_round_two', 'qualify_round_two'),
        })
    )

admin.site.register(Team, TeamAdmin)
