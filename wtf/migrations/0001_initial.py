# Generated by Django 4.1.3 on 2022-12-01 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(choices=[('England', 'England'), ('Scotland', 'Scotland'), ('Wales', 'Wales'), ('Northern Ireland', 'Northern Ireland')], default='England', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wtf.county')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address1', models.CharField(max_length=250)),
                ('address2', models.CharField(blank=True, max_length=250)),
                ('address3', models.CharField(blank=True, max_length=250)),
                ('postcode', models.CharField(max_length=10)),
                ('latitude', models.FloatField(null=True)),
                ('longtitude', models.FloatField(null=True)),
                ('disabledAccess', models.BooleanField()),
                ('description', models.TextField(blank=True)),
                ('town', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='wtf.town')),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=10)),
                ('startTime', models.TimeField()),
                ('duration', models.DurationField()),
                ('description', models.TextField(blank=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wtf.group')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wtf.venue')),
            ],
        ),
        migrations.CreateModel(
            name='Ig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wtf.region')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='ig',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wtf.ig'),
        ),
    ]
