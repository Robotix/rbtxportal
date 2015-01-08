from django import forms
from django.db import models
from participant.models import Participant
from django.utils.translation import ugettext_lazy as _

# Create your models here.

EVENT_CHOICES = [
	('CA' , 'Cascade'),
	('SK' , 'SkyFall'),
	('MI' , 'MineField'),
	('ST' , 'StepUp'),
	('AU' , 'Aug-Hit'),
	('SU' , 'Sudocode'),
]

class Team(models.Model):
    number = models.IntegerField(blank=False)
    event = models.CharField(
    	max_length=3,
    	choices=EVENT_CHOICES,
    	blank=False)
    participant = models.ManyToManyField(Participant)
    certificate_given = models.BooleanField(default=False)
    
    def __unicode__(self):
        return '%s-%s' %(self.event, self.id)

# class TeamForm(forms.Form):
    
