# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150707_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpessoa',
            name='contador2',
            field=models.IntegerField(default=0, editable=False, auto_created=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='contador2',
            field=models.IntegerField(default=0, editable=False, auto_created=True),
        ),
    ]
