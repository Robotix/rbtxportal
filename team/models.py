from django import forms
from django.db import models
from participant.models import Participant
from django.utils.translation import ugettext_lazy as _
from simple_history.models import HistoricalRecords

# Create your models here.

STATES_CHOICES = [
    ('IN-AP' , 'Andhra Pradesh'),
    ('IN-AR' , 'Arunachal Pradesh'),
    ('IN-AS' , 'Assam'),
    ('IN-BR' , 'Bihar'),
    ('IN-CT' , 'Chhattisgarh'),
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
    ('IN-DL' , 'Delhi'),
    ('IN-LD' , 'Lakshadweep'),
    ('IN-PY' , 'Puducherry'),
]

EVENT_CHOICES = [
	('CA' , 'Cascade'),
	('SK' , 'SkyFall'),
	('MI' , 'MineField'),
	('ST' , 'StepUp'),
	('AU' , 'Aug-Hit'),
	('SU' , 'Sudocode'),
]


PARTICIPATION_CHOICES = [
    (0 , 'Select'),
    (1 , 'One'),
    (2 , 'Two'),
    (3 , 'Three'),
    (4 , 'Four'),
]

class Team(models.Model):
    number = models.IntegerField(blank=False)
    participant_number = models.IntegerField(
        choices=PARTICIPATION_CHOICES,
        blank=False,)
    event = models.CharField(
    	max_length=3,
    	choices=EVENT_CHOICES,
    	blank=False)
    participant = models.ManyToManyField(Participant)
    # Address
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
    
    def __unicode__(self):
        return '%s-%s' %(self.event, self.number)

class TeamForm(forms.Form):
    event = forms.ChoiceField(
        widget = forms.Select,
        choices = EVENT_CHOICES)
    number_of_participants = forms.ChoiceField(
        widget = forms.Select, 
        choices = PARTICIPATION_CHOICES)
    participant_id_1 = forms.IntegerField(
        required = True,
        widget = forms.TextInput(attrs={'id':'1', 'required':'True', 'placeholder':'required', 'size':'20'}))
    participant_id_2 = forms.IntegerField(
        required = False,
        widget = forms.TextInput(attrs={'id':'2', 'placeholder':'optional', 'size':'20'}))
    participant_id_3 = forms.IntegerField(
        required = False,
        widget = forms.TextInput(attrs={'id':'3', 'placeholder':'optional', 'size':'20'}))
    participant_id_4 = forms.IntegerField(
        required = False,
        widget = forms.TextInput(attrs={'id':'4', 'placeholder':'optional', 'size':'20'}))    
    street = forms.CharField(
        required = True,
        widget = forms.TextInput(attrs={'required':'True', 'placeholder':'Complete', 'size':'75'}))
    locality = forms.CharField(
        required = True,
        widget = forms.TextInput(attrs={'required':'True', 'placeholder':'Postal', 'size':'75'}))
    city = forms.CharField(
        required = True,
        widget = forms.TextInput(attrs={'required':'True', 'placeholder':'Address','size':'75'}))
    state = forms.ChoiceField(
        widget = forms.Select, 
        choices = STATES_CHOICES)
    pin = forms.IntegerField(
        required = True,
        widget = forms.TextInput(attrs={'required':'True', 'placeholder':'Required','size':'20'}))


class FindForm(forms.Form):
    event = forms.ChoiceField(
        widget = forms.Select,
        choices = EVENT_CHOICES)
    participant_id = forms.IntegerField(
        required = True,
        widget = forms.TextInput(attrs={'required':'True', 'placeholder':'Any one participant\'s ID','size':'20'}))