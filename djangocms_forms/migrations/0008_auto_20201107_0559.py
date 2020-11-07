# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_forms', '0007_auto_20201107_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdefinition',
            name='Recipient_email_Body',
            field=models.TextField(verbose_name='Email Body Text', blank=True),
        ),
    ]
