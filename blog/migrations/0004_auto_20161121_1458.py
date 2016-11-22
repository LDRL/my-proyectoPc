# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20161121_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computadora',
            name='imagen',
            field=models.ImageField(upload_to='blog/fotos', null=True, blank=True),
        ),
    ]
