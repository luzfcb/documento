# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150707_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpessoa',
            name='contador2',
            field=models.IntegerField(default=0, auto_created=True),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='contador2',
            field=models.IntegerField(default=0, auto_created=True),
        ),
    ]
