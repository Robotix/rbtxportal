from django.http import HttpResponse
from django.contrib import admin
from django import forms

from import_export.admin import ExportMixin
from django_object_actions import DjangoObjectActions

from .models import *


class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = '__all__'

    def clean(self):
        if self.cleaned_data['participant'].count() > self.Meta.model.max_team_size:
            raise forms.ValidationError(
                'Max team size is '+str(self.Meta.model.max_team_size),
                code='invalid'
            )


@admin.register(Summit)
@admin.register(Warehouse)
@admin.register(Sherlock)
@admin.register(Sheldon)
@admin.register(DroidBlitz)
class TeamAdmin(ExportMixin, DjangoObjectActions, admin.ModelAdmin):
    search_fields = [
        '=participants__first_name',
        '=participants__last_name',
        'participants__email',
        'participants__mobile',
    ]
    actions = [
        'verify',
        'qualify_to_round_two',
        'qualify_to_round_three',
    ]
    objectactions = [
        'verify_this',
        'qualify_this',
        'print_this',
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
                    ('name',),
                    ('street', 'locality'),
                    ('city', 'pin'),
                    ('state', 'country'),
                ),
                'classes': ('wide'),
            }),
            ('Scoring', {
                'fields': (
                    ('round_one',),
                    ('round_two', 'qualify_round_one',),
                    ('round_three', 'qualify_round_two',),
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
            'qualify_round_one',
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

    def verify(self, request, queryset):
        rows = queryset.update(verification=True)
        self.message_user(request,  '{} teams marked as verified'.format(rows))
    verify.short_description = 'Verify selected teams'

    def qualify_to_round_two(self, request, queryset):
        rows = queryset.update(qualify_round_one=True)
        self.message_user(request, '{} teams are qualified to Round Two')
    qualify_to_round_two.short_description = 'Qualify these teams to Round Two'

    def qualify_to_round_three(self, request, queryset):
        rows = queryset.update(qualify_round_two=True)
        self.message_user(request, '{} teams are qualified to Round Three')
    qualify_to_round_three.short_description = 'Qualify these teams to Round Three'

    def print_this(self, request, team):
        from reportlab.pdfgen import canvas
        from reportlab.lib.units import inch
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Certificate-{}.pdf"'.format(team)
        p = canvas.Canvas(response)
        text_obj = p.beginText()
        text_obj.setFont('Helvetica-Oblique', 14)
        text_obj.setTextOrigin(2*inch, 6.6*inch)
        text_obj.textLine(team.participant.first().name)

        p.drawText(text_obj)
        p.showPage()
        p.save()
        return response
    print_this.label = 'Print Certificates'

    def verify_this(self, request, team):
        team.verification=True
        team.save()
    verify_this.label = 'Verify'

    def qualify_this(self, request, team):
        if team.qualify_round_one:
            team.qualify_round_two = True
        else:
            team.qualify_round_one = True
        team.save()
    qualify_this.label = 'Qualify to the next Round'
