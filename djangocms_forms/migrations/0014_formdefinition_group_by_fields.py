# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_forms', '0013_auto_20201208_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdefinition',
            name='group_by_fields',
            field=models.TextField(verbose_name='Nach diesen Feldern gruppieren', blank=True, default='', help_text='Bitte ein Feld-Name pro Zeile.'),
        ),
    ]
