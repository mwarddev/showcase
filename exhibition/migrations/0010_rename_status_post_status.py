# Generated by Django 3.2 on 2022-03-04 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0009_post_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Status',
            new_name='status',
        ),
    ]
