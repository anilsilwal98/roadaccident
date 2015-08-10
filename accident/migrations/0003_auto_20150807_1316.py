# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accident', '0002_jpt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('streetname', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('cause', models.CharField(max_length=200)),
                ('location', models.ForeignKey(to='accident.Location')),
            ],
        ),
        migrations.DeleteModel(
            name='Jpt',
        ),
    ]
