# Generated by Django 3.2 on 2022-02-18 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0002_alter_post_media'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
