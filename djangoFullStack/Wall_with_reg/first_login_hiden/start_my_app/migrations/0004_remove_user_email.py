# Generated by Django 2.2.4 on 2021-05-29 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('start_my_app', '0003_auto_20210527_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]
