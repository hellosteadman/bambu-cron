# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('next_run', models.DateTimeField()),
                ('name', models.CharField(unique=True, max_length=255)),
                ('running', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('name',),
                'db_table': 'cron_job',
            },
        ),
    ]
