# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20161106_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computadora',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='fotos', null=True),
        ),
    ]
