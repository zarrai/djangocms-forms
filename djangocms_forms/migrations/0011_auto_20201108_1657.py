# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_forms', '0010_auto_20201107_0619'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formdefinition',
            old_name='Recipient_email_Body',
            new_name='confirmation_email_body',
        ),
        migrations.RenameField(
            model_name='formdefinition',
            old_name='Recipient_email_subject',
            new_name='confirmation_email_subject',
        ),
        migrations.RenameField(
            model_name='formdefinition',
            old_name='Recipient_email',
            new_name='confirmation_email_recipient',
        ),
    ]
