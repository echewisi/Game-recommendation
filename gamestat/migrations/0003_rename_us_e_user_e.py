# Generated by Django 4.1.2 on 2022-10-16 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestat', '0002_rename_user_e_us_e'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Us_E',
            new_name='User_E',
        ),
    ]