# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='conteudo',
        ),
        migrations.AddField(
            model_name='documentcontent',
            name='conteudo',
            field=models.OneToOneField(related_name='conteudo', null=True, on_delete=django.db.models.deletion.SET_NULL, editable=False, to='core.Document'),
        ),
        migrations.AddField(
            model_name='historicaldocumentcontent',
            name='conteudo',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='core.Document', null=True),
        ),
    ]
