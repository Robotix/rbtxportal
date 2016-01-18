from django.db import models
from django.core.exceptions import ValidationError

from participant.models import Participant
from miscellaneous.models import College, State


class Team(models.Model):
    participant = models.ManyToManyField(
        Participant,
        verbose_name='Team Members',
        related_name='%(app_label)s_%(class)s_related',
        help_text='<strong>Type in team member\'s name, mobile or e-mail to begin a search</strong><br>'
    )
    max_team_size = 4

    street      = models.CharField(max_length=100, blank=False)
    locality    = models.CharField(max_length=100, blank=False)
    city        = models.CharField(max_length=100, blank=False)
    state       = models.ForeignKey(State)
    pin         = models.IntegerField(blank=False)

    certificate = models.BooleanField(
        default=False,
        verbose_name='Given certificate'
    )
    verification = models.BooleanField(
        default=False,
        verbose_name='Verified'
    )

    round_one = models.IntegerField(
        null=True,
        blank = True,
        verbose_name='Round One Score'
    )
    qualify_round_one = models.BooleanField(
        default = False,
        verbose_name='Qualified Round One'
    )
    round_two = models.IntegerField(
        null=True,
        blank = True,
        verbose_name='Round Two Score'
    )
    qualify_round_two = models.BooleanField(
        default = False,
        verbose_name='Qualified Round Two'
    )
    round_three = models.IntegerField(
        null=True,
        blank = True,
        verbose_name='Round Three Score'
    )

    def __str__(self):
        return '{}-{}'.format(self.event, self.pk)

    class Meta:
        abstract = True


class DroidBlitz(Team):
    event = 'DB'
    max_team_size = 5

    class Meta:
        verbose_name = 'Droid Blitz'
        verbose_name_plural = verbose_name


class Summit(Team):
    event = 'SM'

    class Meta:
        verbose_name = 'Summit'
        verbose_name_plural = verbose_name


class Sherlock(Team):
    event = 'SK'

    class Meta:
        verbose_name = 'Sherlock'
        verbose_name_plural = verbose_name


class Sheldon(Team):
    event ='SD'

    class Meta:
        verbose_name = 'S.H.E.L.D.O.N.'
        verbose_name_plural = verbose_name


class Warehouse(Team):
    event = 'WR'

    class Meta:
        verbose_name = 'Warehouse'
        verbose_name_plural = verbose_name
