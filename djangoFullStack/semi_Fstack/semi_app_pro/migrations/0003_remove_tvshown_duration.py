# Generated by Django 2.2.4 on 2021-05-25 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('semi_app_pro', '0002_auto_20210525_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tvshown',
            name='duration',
        ),
    ]