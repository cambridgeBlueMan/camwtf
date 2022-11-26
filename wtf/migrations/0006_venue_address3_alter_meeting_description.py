# Generated by Django 4.1.3 on 2022-11-26 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wtf', '0005_alter_venue_lattitude_alter_venue_longitude_meeting'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='address3',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
