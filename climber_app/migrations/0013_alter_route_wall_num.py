# Generated by Django 4.2.10 on 2024-04-08 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climber_app', '0012_alter_route_wall_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='wall_num',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
