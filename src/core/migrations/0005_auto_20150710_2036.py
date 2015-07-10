# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150710_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foto',
            name='comentario',
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
        migrations.DeleteModel(
            name='Foto',
        ),
    ]
