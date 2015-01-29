from django import forms
from django.db import models
from participant.models import Participant
from django.utils.translation import ugettext_lazy as _
from simple_history.models import HistoricalRecords
from cascade_round_one.models import Cascade_round_one
from cascade_round_two.models import Cascade_round_two

# Create your models here.

STATES_CHOICES = [
    ('IN-AP' , 'Andhra Pradesh'),
    ('IN-AR' , 'Arunachal Pradesh'),
    ('IN-AS' , 'Assam'),
    ('IN-BR' , 'Bihar'),
    ('IN-CT' , 'Chhattisgarh'),
    ('IN-DL' , 'Delhi'),
    ('IN-GA' , 'Goa'),
    ('IN-GJ' , 'Gujarat'),
    ('IN-HR' , 'Haryana'),
    ('IN-HP' , 'Himachal Pradesh'),
    ('IN-JK' , 'Jammu and Kashmir'),
    ('IN-JH' , 'Jharkhand'),
    ('IN-KA' , 'Karnataka'),
    ('IN-KL' , 'Kerala'),
    ('IN-MP' , 'Madhya Pradesh'),
    ('IN-MH' , 'Maharashtra'),
    ('IN-MN' , 'Manipur'),
    ('IN-ML' , 'Meghalaya'),
    ('IN-MZ' , 'Mizoram'),
    ('IN-NL' , 'Nagaland'),
    ('IN-OR' , 'Odisha'),
    ('IN-PB' , 'Punjab'),
    ('IN-RJ' , 'Rajasthan'),
    ('IN-SK' , 'Sikkim'),
    ('IN-TN' , 'Tamil Nadu'),
    ('IN-TG' , 'Telangana'),
    ('IN-TR' , 'Tripura'),
    ('IN-UT' , 'Uttarakhand'),
    ('IN-UP' , 'Uttar Pradesh'),
    ('IN-WB' , 'West Bengal'),
    ('IN-AN' , 'Andaman and Nicobar Islands'),
    ('IN-CH' , 'Chandigarh'),
    ('IN-DN' , 'Dadra and Nagar Haveli'),
    ('IN-DD' , 'Daman and Diu'),
    ('IN-LD' , 'Lakshadweep'),
    ('IN-PY' , 'Puducherry'),
]

EVENT_CHOICES = (
	('CA' , 'Cascade'),
	('SF' , 'SkyFall'),
	('MF' , 'MineField'),
	('SU' , 'StepUp'),
	('AU' , 'Aug-Hit'),
)


PARTICIPATION_CHOICES = (
    (0 , '------'),
    (1 , 'One'),
    (2 , 'Two'),
    (3 , 'Three'),
    (4 , 'Four'),
)

class Team(models.Model):
    number = models.IntegerField(
        blank=False)
    participant_number = models.IntegerField(
        choices=PARTICIPATION_CHOICES,
        blank=False,)
    event = models.CharField(
    	max_length=3,
    	choices=EVENT_CHOICES,
    	blank=False)
    participant = models.ManyToManyField(Participant, related_name='team')

    '''
        Address Fields.
        '''
    street = models.CharField(
        max_length=100, 
        blank=False)
    locality = models.CharField(max_length=100, blank=False)
    city = models.CharField(max_length=100, blank=False)
    state = models.CharField(
        max_length=5,
        choices= STATES_CHOICES, 
        blank=False)
    pin = models.DecimalField(
        max_digits=6,
        decimal_places=0,
        blank=False)

    certificate_given = models.BooleanField(
        default=False)
    verified = models.BooleanField(
        default=False)
    history = HistoricalRecords()

    '''
        Relational database entries for storing scores for each round.
        '''
    cascade_round_one = models.ForeignKey(
        Cascade_round_one,
        null = True,
        blank = True,)
    qualify_round_one = models.BooleanField(
        default = False,)
    cascade_round_two = models.ForeignKey(
        Cascade_round_two,
        null = True,
        blank = True,)
    qualify_round_two = models.BooleanField(
        default = False)
        
    def __unicode__(self):
        return '%s-%s' %(self.event, self.number)

    def __participant_names__(self):
        names = ''
        for i in self.participant.all():
            names += (i.__unicode__() + ', ')
        return names


class TeamForm(forms.Form):
    event = forms.ChoiceField(
        widget = forms.Select,
        choices = EVENT_CHOICES)
    number_of_participants = forms.ChoiceField(
        widget = forms.Select(attrs={'id':'opt', 'onchange':'showFields()'}), 
        choices = PARTICIPATION_CHOICES)
    participant_no_1 = forms.IntegerField(
        label= 'Enter participant IDs', 
        required = True,
        widget = forms.TextInput(attrs={'id':'one', 'style':'display: none;', 'title':'Please select at least one participant', 'x-moz-errormessage':'Select at least one participant', 'required':'True', 'placeholder':'required', 'size':'20'}))
    participant_no_2 = forms.IntegerField(
        label= '', 
        required = False,
        widget = forms.TextInput(attrs={'id':'two', 'style':'display: none;', 'placeholder':'required', 'size':'20'}))
    participant_no_3 = forms.IntegerField(
        label= '', 
        required = False,
        widget = forms.TextInput(attrs={'id':'three', 'style':'display: none;', 'placeholder':'required', 'size':'20'}))
    participant_no_4 = forms.IntegerField(
        label= '', 
        required = False,
        widget = forms.TextInput(attrs={'id':'four', 'style':'display: none;', 'placeholder':'required', 'size':'20'}))    
    street = forms.CharField(
        required = True,
        widget = forms.TextInput(attrs={'required':'True', 'placeholder':'Complete', 'size':'75'}))
    locality = forms.CharField(
        required = True,
        widget = forms.TextInput(attrs={'required':'True', 'placeholder':'Postal', 'size':'75'}))
    city = forms.CharField(
        required = True,
        widget = forms.TextInput(attrs={'required':'True', 'placeholder':'Address','size':'75'}))
    pin = forms.IntegerField(
        required = True,
        widget = forms.TextInput(attrs={'required':'True', 'pattern':'[1-9][0-9][0-9][0-9][0-9][0-9]', 'title':'Enter 6 digit PIN', 'placeholder':'Required','size':'20'}))
    state = forms.ChoiceField(
        widget = forms.Select, 
        choices = STATES_CHOICES)

    class Meta:
        fieldsets = [
            (_('Team Info'), {'fields': ('event', 'number_of_participants', 'participant_no_1', 'participant_no_2', 'participant_no_3', 'participant_no_4')}),
            (_('Address'), {'fields': ('street','locality', 'city', 'pin', 'state')}),
        ]


class FindForm(forms.Form):
    event = forms.ChoiceField(
        widget = forms.Select,
        choices = EVENT_CHOICES)
    participant_id = forms.IntegerField(
        required = True,
        widget = forms.TextInput(attrs={'required':'True', 'placeholder':'Any one participant\'s ID','size':'20'}))