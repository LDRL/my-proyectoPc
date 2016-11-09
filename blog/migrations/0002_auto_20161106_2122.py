# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='activo',
            field=models.BooleanField(editable=False, default=True),
        ),
        migrations.AddField(
            model_name='computadora',
            name='activo',
            field=models.BooleanField(editable=False, default=True),
        ),
        migrations.AddField(
            model_name='marca',
            name='activo',
            field=models.BooleanField(editable=False, default=True),
        ),
    ]
