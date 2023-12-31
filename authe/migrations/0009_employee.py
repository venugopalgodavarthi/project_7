# Generated by Django 4.2.6 on 2023-10-26 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authe', '0008_constraints'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('eid', models.SmallAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.PositiveBigIntegerField(unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField(null=True)),
            ],
        ),
    ]
