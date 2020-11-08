# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_forms', '0011_auto_20201108_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdefinition',
            name='confirmation_email_recipient',
            field=models.CharField(verbose_name='Recipient e-mail address field name', max_length=255, blank=True, help_text="Copy here the name of the form field containing the recipient's email address."),
        ),
    ]
