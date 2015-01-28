from django.db import models

# Create your models here.

points = {
	'terrorist_shot'	: +75,
	'civilian_shot'		: -25,
	'manual_reload'		: -20,
	'timeout'			: -50,
	'restart'			: -100,
	'time'				: -1,
}

class Cascade_round_one(models.Model):
	terrorist_shot = models.IntegerField(
		blank = False,)
	civilian_shot = models.IntegerField(
		blank = False,)
	manual_reload = models.IntegerField(
		blank = False,)
	timeout = models.IntegerField(
		blank = False,)
	restart = models.IntegerField(
		blank = False,)
	time = models.IntegerField(
		blank = False,)
	remarks = models.CharField(
		max_length=255,
		blank = True)

	def score(self):
		score = (
			180 + 
			points['terrorist_shot']*self.terrorist_shot +
			points['civilian_shot']*self.civilian_shot +
			points['manual_reload']*self.manual_reload +
			points['timeout']*self.timeout +
			points['restart']*self.restart +
			points['time']*self.time 
		)
		return score

	def __unicode__(self):
		return str(self.score())