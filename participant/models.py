from django import forms
from django.db import models
from django.utils.translation import ugettext_lazy as _
from simple_history.models import HistoricalRecords

# Create your models here.

YEAR_CHOICES = (
    (1,'First'),
    (2,'Second'), 
    (3,'Third'), 
    (4,'Fourth'),
    (5,'Fifth'),
)

class Participant(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50, blank= False)
    lastName = models.CharField(max_length=50, blank=False)
    mobileNo = models.DecimalField(
        max_digits=13,
        decimal_places=0,
        blank=False)
    emailID = models.EmailField(blank=False)
    year = models.IntegerField(blank=False, choices=YEAR_CHOICES)
    college = models.CharField(max_length=255, blank=False)

    history = HistoricalRecords()
    
    def __team__(self):
        team_str = ''
        for i in self.team.all():
            team_str += (i.__unicode__()+', ')
        return team_str

    def __unicode__(self):
        return str(self.id) + '-' + self.firstName + ' ' + self.lastName

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields= '__all__'
        labels = {
            'firstName': _('First Name'),
            'lastName': _('Last Name'),
            'mobileNo': _('Mobile Number'),
            'emailID': _('EMail ID'),
            'year': _('Year of Study'),
            'college': _('College'),
        }
        widgets = {
            'firstName': forms.TextInput(attrs={'required':'True', 'placeholder':'First Name','size':'50'}),
            'lastName': forms.TextInput(attrs={'required':'True', 'placeholder':'Last Name','size':'50'}),
            'mobileNo': forms.TextInput(attrs={'required':'True', 'pattern':'[7-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]', 'title':'Enter 10 digit valid mobile number','placeholder':'10 digit Mobile Number','maxlength':'10', 'size':'50'}),
            'emailID': forms.EmailInput(attrs={'required':'True', 'placeholder':'email@domain.com','size':'50'}),
            'college': forms.TextInput(attrs={'required':'True', 'placeholder':'College','size':'50'}),
        }

class FindForm(forms.Form):
    participant_mobile = forms.IntegerField(
        required = True,
        label='',
        widget = forms.TextInput(attrs={'required':'True', 'placeholder':'Enter your 10 digit Mobile Number','maxlength':'10', 'size':'50'}))