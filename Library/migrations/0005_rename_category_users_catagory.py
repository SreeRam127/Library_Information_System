# Generated by Django 3.2.5 on 2022-07-20 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0004_rename_catagory_users_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='category',
            new_name='catagory',
        ),
    ]
