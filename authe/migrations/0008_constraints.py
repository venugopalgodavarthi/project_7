# Generated by Django 4.2.6 on 2023-10-26 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authe', '0007_boolmodels'),
    ]

    operations = [
        migrations.CreateModel(
            name='constraints',
            fields=[
                ('sid', models.BigAutoField(primary_key=True, serialize=False)),
                ('phone', models.PositiveBigIntegerField(unique=True)),
                ('age', models.PositiveSmallIntegerField(null=True)),
                ('gender', models.CharField(default='Male', max_length=10)),
                ('subject', models.CharField(choices=[['python', 'Python'], ['django', 'django']], max_length=50)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authe.student')),
            ],
        ),
    ]
