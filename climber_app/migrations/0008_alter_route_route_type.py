# Generated by Django 4.2.10 on 2024-04-07 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climber_app', '0007_rename_type_route_route_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='route_type',
            field=models.CharField(max_length=20),
        ),
    ]
