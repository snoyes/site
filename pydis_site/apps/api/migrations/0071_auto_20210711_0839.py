# Generated by Django 3.0.14 on 2021-07-11 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0070_new_filter_schema'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filterlist',
            name='list_type',
            field=models.IntegerField(choices=[(1, 'Allow'), (0, 'Deny')], help_text='Whether this list is an allowlist or denylist'),
        ),
        migrations.AlterField(
            model_name='filtersettings',
            name='default_action',
            field=models.ForeignKey(help_text='What action to perform on the triggering user.', on_delete=django.db.models.deletion.CASCADE, to='api.FilterAction'),
        ),
        migrations.AlterField(
            model_name='filtersettings',
            name='default_range',
            field=models.ForeignKey(help_text='The channels and categories in which this filter applies.', on_delete=django.db.models.deletion.CASCADE, to='api.ChannelRange'),
        ),
        migrations.AlterField(
            model_name='filtersettings',
            name='delete_messages',
            field=models.BooleanField(help_text='Whether this filter should delete messages triggering it.'),
        ),
        migrations.AlterField(
            model_name='filtersettings',
            name='enabled',
            field=models.BooleanField(help_text='Whether this filter is currently enabled.'),
        ),
        migrations.AlterField(
            model_name='filtersettings',
            name='filter_dm',
            field=models.BooleanField(help_text='Whether DMs should be filtered.'),
        ),
    ]