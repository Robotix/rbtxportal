from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class State(models.Model):
    name    = models.CharField(max_length=20)
    country = models.ForeignKey(Country)

    def __str__(self):
        return self.name


class College(models.Model):
    name  = models.CharField(
        max_length=100,
        blank=False,
        verbose_name='College Name'
    )
    abbv  = models.CharField(
        max_length=30,
        blank=False,
        verbose_name='Abbreviation'
    )
    city  = models.CharField(max_length=20, blank=False)
    state = models.ForeignKey(State)

    @staticmethod
    def autocomplete_search_fields():
        return 'name', 'abbv'

    def __str__(self):
        return '{}, {}'.format(self.name, self.city)
