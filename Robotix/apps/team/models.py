from django.db import models
from django.core.exceptions import ValidationError

from participant.models import Participant
from miscellaneous.models import College, State, Country


class Team(models.Model):
    participant = models.ManyToManyField(
        Participant,
        verbose_name='Team Members',
        related_name='%(app_label)s_%(class)s_related',
        help_text='<strong>Type in team member\'s name, mobile or e-mail to begin a search</strong><br>'
    )
    max_team_size = 4

    name        = models.CharField(
        max_length=50,
        blank=False,
        verbose_name='Receiver\'s Name',
        help_text='Provide Team leader\'s or caretaker\'s full name'
    )
    street      = models.CharField(max_length=100, blank=False)
    locality    = models.CharField(max_length=100, blank=False)
    city        = models.CharField(max_length=100, blank=False)
    state       = models.ForeignKey(State)
    country     = models.ForeignKey(Country,
        default=1
    )
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
        verbose_name='Qualified for Round Two'
    )
    round_two = models.IntegerField(
        null=True,
        blank = True,
        verbose_name='Round Two Score'
    )
    qualify_round_two = models.BooleanField(
        default = False,
        verbose_name='Qualified for Round Three'
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
        verbose_name = 'Droid Blitz Team'


class Summit(Team):
    event = 'SM'

    class Meta:
        verbose_name = 'Summit Team'


class Sherlock(Team):
    event = 'SK'

    class Meta:
        verbose_name = 'Sherlock Team'


class Sheldon(Team):
    event ='SD'

    class Meta:
        verbose_name = 'S.H.E.L.D.O.N. Team'


class Warehouse(Team):
    event = 'WR'

    class Meta:
        verbose_name = 'Warehouse Team'
