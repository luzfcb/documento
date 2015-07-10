# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_comentario_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='comentario',
            field=models.ForeignKey(to='core.Comentario'),
        ),
    ]
