# Generated by Django 2.2.6 on 2019-10-31 12:14

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0047_deletedmessage_attachments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deletedmessage',
            name='attachments',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=512), blank=True, help_text='Attachments attached to this message.', size=None),
        ),
    ]
