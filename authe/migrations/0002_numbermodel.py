# Generated by Django 4.2.6 on 2023-10-26 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='numbermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num1', models.IntegerField()),
                ('num4', models.PositiveBigIntegerField()),
                ('num5', models.FloatField()),
                ('num6', models.DecimalField(decimal_places=3, max_digits=5)),
                ('num7', models.GenericIPAddressField()),
            ],
        ),
    ]
