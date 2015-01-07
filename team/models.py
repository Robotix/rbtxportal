from django.db import models
from address.models import Address
from participant.models import Participant

# Create your models here.

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.CharField(max_length=3)
    participants = models.ManyToManyField(Participant)
    certificate_given = models.BooleanField(default=False)
    
    def getTeamID(self):
        return '%s-%s' %(self.event, self.id)