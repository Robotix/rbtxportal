# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cascade_round_one', '__first__'),
        ('participant', '__first__'),
        ('cascade_round_two', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalTeam',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('number', models.IntegerField()),
                ('participant_number', models.IntegerField(choices=[(0, b'------'), (1, b'One'), (2, b'Two'), (3, b'Three'), (4, b'Four')])),
                ('event', models.CharField(max_length=3, choices=[(b'CA', b'Cascade'), (b'SK', b'SkyFall'), (b'MI', b'MineField'), (b'ST', b'StepUp'), (b'AU', b'Aug-Hit')])),
                ('street', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=5, choices=[(b'IN-AP', b'Andhra Pradesh'), (b'IN-AR', b'Arunachal Pradesh'), (b'IN-AS', b'Assam'), (b'IN-BR', b'Bihar'), (b'IN-CT', b'Chhattisgarh'), (b'IN-DL', b'Delhi'), (b'IN-GA', b'Goa'), (b'IN-GJ', b'Gujarat'), (b'IN-HR', b'Haryana'), (b'IN-HP', b'Himachal Pradesh'), (b'IN-JK', b'Jammu and Kashmir'), (b'IN-JH', b'Jharkhand'), (b'IN-KA', b'Karnataka'), (b'IN-KL', b'Kerala'), (b'IN-MP', b'Madhya Pradesh'), (b'IN-MH', b'Maharashtra'), (b'IN-MN', b'Manipur'), (b'IN-ML', b'Meghalaya'), (b'IN-MZ', b'Mizoram'), (b'IN-NL', b'Nagaland'), (b'IN-OR', b'Odisha'), (b'IN-PB', b'Punjab'), (b'IN-RJ', b'Rajasthan'), (b'IN-SK', b'Sikkim'), (b'IN-TN', b'Tamil Nadu'), (b'IN-TG', b'Telangana'), (b'IN-TR', b'Tripura'), (b'IN-UT', b'Uttarakhand'), (b'IN-UP', b'Uttar Pradesh'), (b'IN-WB', b'West Bengal'), (b'IN-AN', b'Andaman and Nicobar Islands'), (b'IN-CH', b'Chandigarh'), (b'IN-DN', b'Dadra and Nagar Haveli'), (b'IN-DD', b'Daman and Diu'), (b'IN-LD', b'Lakshadweep'), (b'IN-PY', b'Puducherry')])),
                ('pin', models.DecimalField(max_digits=6, decimal_places=0)),
                ('certificate_given', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('cascade_round_one_id', models.IntegerField(db_index=True, null=True, blank=True)),
                ('qualify_round_one', models.BooleanField(default=False)),
                ('cascade_round_two_id', models.IntegerField(db_index=True, null=True, blank=True)),
                ('qualify_round_two', models.BooleanField(default=False)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical team',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
                ('participant_number', models.IntegerField(choices=[(0, b'------'), (1, b'One'), (2, b'Two'), (3, b'Three'), (4, b'Four')])),
                ('event', models.CharField(max_length=3, choices=[(b'CA', b'Cascade'), (b'SK', b'SkyFall'), (b'MI', b'MineField'), (b'ST', b'StepUp'), (b'AU', b'Aug-Hit')])),
                ('street', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=5, choices=[(b'IN-AP', b'Andhra Pradesh'), (b'IN-AR', b'Arunachal Pradesh'), (b'IN-AS', b'Assam'), (b'IN-BR', b'Bihar'), (b'IN-CT', b'Chhattisgarh'), (b'IN-DL', b'Delhi'), (b'IN-GA', b'Goa'), (b'IN-GJ', b'Gujarat'), (b'IN-HR', b'Haryana'), (b'IN-HP', b'Himachal Pradesh'), (b'IN-JK', b'Jammu and Kashmir'), (b'IN-JH', b'Jharkhand'), (b'IN-KA', b'Karnataka'), (b'IN-KL', b'Kerala'), (b'IN-MP', b'Madhya Pradesh'), (b'IN-MH', b'Maharashtra'), (b'IN-MN', b'Manipur'), (b'IN-ML', b'Meghalaya'), (b'IN-MZ', b'Mizoram'), (b'IN-NL', b'Nagaland'), (b'IN-OR', b'Odisha'), (b'IN-PB', b'Punjab'), (b'IN-RJ', b'Rajasthan'), (b'IN-SK', b'Sikkim'), (b'IN-TN', b'Tamil Nadu'), (b'IN-TG', b'Telangana'), (b'IN-TR', b'Tripura'), (b'IN-UT', b'Uttarakhand'), (b'IN-UP', b'Uttar Pradesh'), (b'IN-WB', b'West Bengal'), (b'IN-AN', b'Andaman and Nicobar Islands'), (b'IN-CH', b'Chandigarh'), (b'IN-DN', b'Dadra and Nagar Haveli'), (b'IN-DD', b'Daman and Diu'), (b'IN-LD', b'Lakshadweep'), (b'IN-PY', b'Puducherry')])),
                ('pin', models.DecimalField(max_digits=6, decimal_places=0)),
                ('certificate_given', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('qualify_round_one', models.BooleanField(default=False)),
                ('qualify_round_two', models.BooleanField(default=False)),
                ('cascade_round_one', models.ForeignKey(blank=True, to='cascade_round_one.Cascade_round_one', null=True)),
                ('cascade_round_two', models.ForeignKey(blank=True, to='cascade_round_two.Cascade_round_two', null=True)),
                ('participant', models.ManyToManyField(to='participant.Participant')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
