# Generated by Django 2.2.4 on 2021-05-30 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start_my_app', '0004_remove_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default=True, max_length=45),
        ),
    ]
