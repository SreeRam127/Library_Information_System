# Generated by Django 3.2.5 on 2022-07-21 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0006_auto_20220721_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='ebook_url',
            field=models.URLField(default=None),
        ),
    ]