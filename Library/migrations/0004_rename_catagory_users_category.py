# Generated by Django 3.2.5 on 2022-07-20 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0003_auto_20220720_1321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='catagory',
            new_name='category',
        ),
    ]