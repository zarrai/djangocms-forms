# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_forms', '0005_formfield_field_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdefinition',
            name='Recipient_email_introtext',
            field=models.CharField(verbose_name='Email Introduction Text', max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='formdefinition',
            name='Recipient_email_subject',
            field=models.CharField(verbose_name='Email Subject', max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='formdefinition',
            name='Recipient_email_to',
            field=models.CharField(verbose_name='Recipient e-mail address', max_length=255, blank=True, help_text='Separate several addresses with a comma.'),
        ),
        migrations.AlterField(
            model_name='formdefinition',
            name='cmsplugin_ptr',
            field=models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='djangocms_forms_formdefinition', parent_link=True, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='formdefinition',
            name='form_template',
            field=models.CharField(verbose_name='Form Template', max_length=150, blank=True, default='djangocms_forms/form_template/default.html', choices=[('djangocms_forms/form_template/default.html', 'Default')]),
        ),
        migrations.AlterField(
            model_name='formdefinition',
            name='spam_protection',
            field=models.SmallIntegerField(verbose_name='Spam Protection', default=0, choices=[(0, 'None'), (1, 'Honeypot')]),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='field_type',
            field=models.CharField(verbose_name='Field Type', max_length=100, default='text', choices=[('text', 'Text'), ('textarea', 'Text Area'), ('email', 'Email'), ('number', 'Number'), ('phone', 'Phone'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkbox_multiple', 'Multi Checkbox'), ('select', 'Drop down'), ('radio', 'Radio'), ('file', 'File Upload'), ('date', 'Date'), ('time', 'Time'), ('password', 'Password'), ('hidden', 'Hidden'), ('headline', 'Zwischenüberschrift')]),
        ),
        migrations.AlterField(
            model_name='formsubmission',
            name='ip',
            field=models.GenericIPAddressField(verbose_name='IP', blank=True, null=True),
        ),
    ]
