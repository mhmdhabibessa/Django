# Generated by Django 2.2.4 on 2021-05-20 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm_app', '0002_auto_20210520_1137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='email_address',
            new_name='email',
        ),
    ]
