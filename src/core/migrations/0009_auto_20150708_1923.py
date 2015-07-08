# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20150708_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpessoa',
            name='conteudo',
            field=redactor.fields.RedactorField(),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='conteudo',
            field=redactor.fields.RedactorField(),
        ),
    ]
