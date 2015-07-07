# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150707_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpessoa',
            name='contador',
            field=core.fields.CounterField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='contador',
            field=core.fields.CounterField(default=None, null=True, blank=True),
        ),
    ]
