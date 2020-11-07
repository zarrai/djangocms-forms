# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_forms', '0009_auto_20201107_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdefinition',
            name='Recipient_email_subject',
            field=models.CharField(verbose_name='Recipient Email Subject', max_length=255, blank=True),
        ),
    ]
