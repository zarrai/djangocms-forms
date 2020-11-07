# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_forms', '0006_auto_20201107_0259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formdefinition',
            name='Recipient_email_introtext',
        ),
        migrations.AddField(
            model_name='formdefinition',
            name='Recipient_email_Body',
            field=models.TextField(verbose_name='Email Body Text', max_length=255, blank=True),
        ),
    ]
