# Generated by Django 4.1.3 on 2022-12-06 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wtf', '0003_remove_meeting_day'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting',
            old_name='dayAsInt',
            new_name='day',
        ),
    ]
