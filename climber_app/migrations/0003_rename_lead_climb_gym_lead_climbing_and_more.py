# Generated by Django 4.2.10 on 2024-04-06 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('climber_app', '0002_remove_gym_route_types_gym_bouldering_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gym',
            old_name='lead_climb',
            new_name='lead_climbing',
        ),
        migrations.RenameField(
            model_name='gym',
            old_name='top_rope',
            new_name='top_rope_climbing',
        ),
    ]
