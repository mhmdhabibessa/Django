# Generated by Django 2.2.4 on 2021-05-23 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninja_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ninja',
            old_name='dojo_id',
            new_name='dojo_id_ninja',
        ),
    ]