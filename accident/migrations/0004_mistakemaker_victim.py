# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accident', '0003_auto_20150807_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mistakemaker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('vehicletype', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('injury', models.CharField(max_length=100)),
                ('case', models.ForeignKey(to='accident.Case')),
            ],
        ),
        migrations.CreateModel(
            name='Victim',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('vehicletype', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('injury', models.CharField(max_length=100)),
                ('case', models.ForeignKey(to='accident.Case')),
            ],
        ),
    ]
