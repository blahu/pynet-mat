# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('net_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SnmpCredentials',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('snmp_version', models.IntegerField(default=2)),
                ('snmp_community', models.CharField(max_length=80)),
                ('snmp_port', models.IntegerField(default=161)),
                ('v3_user', models.CharField(max_length=80, null=True, blank=True)),
                ('v3_auth_key', models.CharField(max_length=80, null=True, blank=True)),
                ('v3_auth_proto', models.CharField(default=b'sha', max_length=80)),
                ('v3_encrypt_key', models.CharField(max_length=80, null=True, blank=True)),
                ('v3_encrypt_proto', models.CharField(default=b'aes128', max_length=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='networkdevice',
            name='snmp',
            field=models.ForeignKey(blank=True, to='net_system.SnmpCredentials', null=True),
            preserve_default=True,
        ),
    ]
