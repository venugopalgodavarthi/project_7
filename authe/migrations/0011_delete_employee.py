# Generated by Django 4.2.6 on 2023-10-26 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authe', '0010_remove_employee_email_remove_employee_phone_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='employee',
        ),
    ]