from django.db import models
from django.core.validators import RegexValidator
from miscellaneous.models import College

from .utils import *


class Participant(models.Model):
    first_name  = models.CharField(max_length=50, blank= False)
    last_name   = models.CharField(max_length=50, blank=False)
    mobile      = models.BigIntegerField(
        blank=False,
        verbose_name='Mobile Number',
        help_text='Do NOT add a 0 or +91',
        validators=[
            RegexValidator('^[789]\d{9}$',
                message='Invalid mobile number<br>Do NOT add a 0 or +91',
            )
        ]
    )
    email       = models.EmailField(blank=False, verbose_name='E-Mail address')
    year        = models.IntegerField(
        blank=False,
        choices=YEAR_CHOICES,
        verbose_name='Year of study'
    )
    college     = models.ForeignKey(College)

    @property
    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @staticmethod
    def autocomplete_search_fields():
        return 'first_name', 'last_name', 'mobile', 'email'

    def __str__(self):
        return self.name
