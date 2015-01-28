from django.db import models

# Create your models here.

class Cascade_round_two(models.Model):
	stationary_terrorist_shot = models.IntegerField(
		blank = False,)
	movingy_terrorist_shot = models.IntegerField(
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

	def __unicode__(self):
		'''
			Returns the total score as a string.
			'''
		return None