# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('event_name', models.CharField(max_length=75)),
                ('event_description', models.CharField(max_length=500)),
                ('event_date', models.DateField()),
                ('event_timings', models.TimeField()),
                ('event_venue', models.CharField(max_length=75)),
                ('event_fees', models.IntegerField(default=0)),
                ('event_steats', models.IntegerField(default=36)),
                ('event_organizer_details', models.CharField(max_length=10)),
            ],
        ),
    ]
