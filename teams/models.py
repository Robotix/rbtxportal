from django.db import models

# Create your models here.

class Participant(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    mobileNo = models.CharField(max_length=13)
    emailID= models.EmailField()
    college = models.CharField(max_length=100)

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.CharField(max_length=3)
    participants = models.ManyToManyField(Participant)
    status = models.CharField(max_length=50, default= '')
    
    def getTeamID(self):
        return '%s-%s' %(self.event, self.id)
