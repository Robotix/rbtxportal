# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0003_auto_20160121_2233'),
        ('miscellaneous', '0001_initial'),
        ('team', '0003_auto_20160121_1821'),
    ]

    operations = [
        migrations.CreateModel(
            name='BombDisposal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name="Receiver's Name", help_text="Provide Team leader's or caretaker's full name", max_length=50)),
                ('street', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pin', models.IntegerField()),
                ('certificate', models.BooleanField(verbose_name='Given certificate', default=False)),
                ('verification', models.BooleanField(verbose_name='Verified', default=False)),
                ('round_one', models.IntegerField(verbose_name='Round One Score', blank=True, null=True)),
                ('qualify_round_one', models.BooleanField(verbose_name='Qualified for Round Two', default=False)),
                ('round_two', models.IntegerField(verbose_name='Round Two Score', blank=True, null=True)),
                ('qualify_round_two', models.BooleanField(verbose_name='Qualified for Round Three', default=False)),
                ('round_three', models.IntegerField(verbose_name='Round Three Score', blank=True, null=True)),
                ('country', models.ForeignKey(default=1, to='miscellaneous.Country')),
                ('participant', models.ManyToManyField(verbose_name='Team Members', related_name='team_bombdisposal_related', to='participant.Participant', help_text="<strong>Type in team member's name, mobile or e-mail to begin a search</strong><br>")),
                ('state', models.ForeignKey(to='miscellaneous.State')),
            ],
            options={
                'verbose_name': 'BombDisposal',
                'verbose_name_plural': 'BombDisposal',
            },
        ),
        migrations.CreateModel(
            name='Bricks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name="Receiver's Name", help_text="Provide Team leader's or caretaker's full name", max_length=50)),
                ('street', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pin', models.IntegerField()),
                ('certificate', models.BooleanField(verbose_name='Given certificate', default=False)),
                ('verification', models.BooleanField(verbose_name='Verified', default=False)),
                ('round_one', models.IntegerField(verbose_name='Round One Score', blank=True, null=True)),
                ('qualify_round_one', models.BooleanField(verbose_name='Qualified for Round Two', default=False)),
                ('round_two', models.IntegerField(verbose_name='Round Two Score', blank=True, null=True)),
                ('qualify_round_two', models.BooleanField(verbose_name='Qualified for Round Three', default=False)),
                ('round_three', models.IntegerField(verbose_name='Round Three Score', blank=True, null=True)),
                ('country', models.ForeignKey(default=1, to='miscellaneous.Country')),
                ('participant', models.ManyToManyField(verbose_name='Team Members', related_name='team_bricks_related', to='participant.Participant', help_text="<strong>Type in team member's name, mobile or e-mail to begin a search</strong><br>")),
                ('state', models.ForeignKey(to='miscellaneous.State')),
            ],
            options={
                'verbose_name': 'B.R.I.C.K.S',
                'verbose_name_plural': 'B.R.I.C.K.S',
            },
        ),
        migrations.CreateModel(
            name='Conquest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name="Receiver's Name", help_text="Provide Team leader's or caretaker's full name", max_length=50)),
                ('street', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pin', models.IntegerField()),
                ('certificate', models.BooleanField(verbose_name='Given certificate', default=False)),
                ('verification', models.BooleanField(verbose_name='Verified', default=False)),
                ('round_one', models.IntegerField(verbose_name='Round One Score', blank=True, null=True)),
                ('qualify_round_one', models.BooleanField(verbose_name='Qualified for Round Two', default=False)),
                ('round_two', models.IntegerField(verbose_name='Round Two Score', blank=True, null=True)),
                ('qualify_round_two', models.BooleanField(verbose_name='Qualified for Round Three', default=False)),
                ('round_three', models.IntegerField(verbose_name='Round Three Score', blank=True, null=True)),
                ('country', models.ForeignKey(default=1, to='miscellaneous.Country')),
                ('participant', models.ManyToManyField(verbose_name='Team Members', related_name='team_conquest_related', to='participant.Participant', help_text="<strong>Type in team member's name, mobile or e-mail to begin a search</strong><br>")),
                ('state', models.ForeignKey(to='miscellaneous.State')),
            ],
            options={
                'verbose_name': 'Conquest',
                'verbose_name_plural': 'Conquest',
            },
        ),
        migrations.RemoveField(
            model_name='droidblitz',
            name='country',
        ),
        migrations.RemoveField(
            model_name='droidblitz',
            name='participant',
        ),
        migrations.RemoveField(
            model_name='droidblitz',
            name='state',
        ),
        migrations.RemoveField(
            model_name='sheldon',
            name='country',
        ),
        migrations.RemoveField(
            model_name='sheldon',
            name='participant',
        ),
        migrations.RemoveField(
            model_name='sheldon',
            name='state',
        ),
        migrations.RemoveField(
            model_name='sherlock',
            name='country',
        ),
        migrations.RemoveField(
            model_name='sherlock',
            name='participant',
        ),
        migrations.RemoveField(
            model_name='sherlock',
            name='state',
        ),
        migrations.RemoveField(
            model_name='summit',
            name='country',
        ),
        migrations.RemoveField(
            model_name='summit',
            name='participant',
        ),
        migrations.RemoveField(
            model_name='summit',
            name='state',
        ),
        migrations.RemoveField(
            model_name='warehouse',
            name='country',
        ),
        migrations.RemoveField(
            model_name='warehouse',
            name='participant',
        ),
        migrations.RemoveField(
            model_name='warehouse',
            name='state',
        ),
        migrations.DeleteModel(
            name='DroidBlitz',
        ),
        migrations.DeleteModel(
            name='Sheldon',
        ),
        migrations.DeleteModel(
            name='Sherlock',
        ),
        migrations.DeleteModel(
            name='Summit',
        ),
        migrations.DeleteModel(
            name='Warehouse',
        ),
    ]
