# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('event', models.CharField(max_length=3)),
                ('certificate_given', models.BooleanField(default=False)),
                ('participants', models.ManyToManyField(to='participant.Participant')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
