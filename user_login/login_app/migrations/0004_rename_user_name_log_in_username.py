# Generated by Django 4.1.1 on 2022-10-14 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0003_rename_username_log_in_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log_in',
            old_name='user_name',
            new_name='username',
        ),
    ]