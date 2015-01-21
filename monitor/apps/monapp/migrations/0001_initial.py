# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('HostName', models.CharField(max_length=50)),
                ('Pri_IP', models.IPAddressField(blank=True)),
                ('Pub_IP', models.IPAddressField(blank=True)),
                ('Serial', models.CharField(max_length=25, serialize=False, primary_key=True)),
                ('OsType', models.CharField(default=b'CentOS6', max_length=10)),
                ('UserName', models.CharField(default=b'root', max_length=15)),
                ('Password', models.CharField(max_length=50, blank=True)),
                ('Region', models.CharField(default=b'Beijing', max_length=20)),
                ('Status', models.SmallIntegerField(default=1, choices=[(0, 'OFF'), (1, 'ON')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('GroupName', models.CharField(default=b'IZPGroup', max_length=50)),
                ('GroupID', models.IntegerField(default=0, max_length=5, serialize=False, primary_key=True)),
                ('Description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='host',
            name='GroupID',
            field=models.ForeignKey(to='monapp.HostGroup'),
            preserve_default=True,
        ),
    ]
