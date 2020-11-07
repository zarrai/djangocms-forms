# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_forms', '0008_auto_20201107_0559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formdefinition',
            old_name='Recipient_email_to',
            new_name='Recipient_email',
        ),
    ]
