# Generated by Django 4.2.6 on 2023-10-26 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authe', '0005_datemodels'),
    ]

    operations = [
        migrations.CreateModel(
            name='filemodels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file1', models.FileField(upload_to='')),
                ('file2', models.ImageField(upload_to='')),
                ('file3', models.FilePathField()),
            ],
        ),
    ]