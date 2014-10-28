# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('net_system', '0002_auto_20141028_1127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='networkdevice',
            old_name='snmp',
            new_name='snmp_creds',
        ),
        migrations.RenameField(
            model_name='snmpcredentials',
            old_name='v3_auth_key',
            new_name='auth_key',
        ),
        migrations.RenameField(
            model_name='snmpcredentials',
            old_name='v3_auth_proto',
            new_name='auth_proto',
        ),
        migrations.RenameField(
            model_name='snmpcredentials',
            old_name='snmp_community',
            new_name='community',
        ),
        migrations.RenameField(
            model_name='snmpcredentials',
            old_name='v3_encrypt_key',
            new_name='encrypt_key',
        ),
        migrations.RenameField(
            model_name='snmpcredentials',
            old_name='v3_encrypt_proto',
            new_name='encrypt_proto',
        ),
        migrations.RemoveField(
            model_name='snmpcredentials',
            name='snmp_port',
        ),
        migrations.RemoveField(
            model_name='snmpcredentials',
            name='snmp_version',
        ),
        migrations.RemoveField(
            model_name='snmpcredentials',
            name='v3_user',
        ),
        migrations.AddField(
            model_name='networkdevice',
            name='snmp_port',
            field=models.IntegerField(default=161),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='snmpcredentials',
            name='version',
            field=models.IntegerField(default=3),
            preserve_default=True,
        ),
    ]
