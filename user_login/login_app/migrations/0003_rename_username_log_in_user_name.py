# Generated by Django 4.1.1 on 2022-10-14 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_rename_user_name_log_in_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log_in',
            old_name='username',
            new_name='user_name',
        ),
    ]