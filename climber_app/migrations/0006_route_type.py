# Generated by Django 4.2.10 on 2024-04-07 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climber_app', '0005_gym_daily_price_gym_membership_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='type',
            field=models.CharField(default=None, max_length=20),
        ),
    ]