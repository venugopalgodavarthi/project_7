# Generated by Django 4.2.6 on 2023-10-26 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authe', '0004_charmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='datemodels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.DateField()),
                ('date2', models.TimeField()),
                ('date3', models.DateTimeField()),
                ('date4', models.DurationField()),
            ],
        ),
    ]