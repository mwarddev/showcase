# Generated by Django 3.2 on 2022-03-18 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0015_alter_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
