# Generated by Django 4.1.3 on 2022-11-30 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wtf', '0009_county_town'),
    ]

    operations = [
        migrations.AddField(
            model_name='town',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
