# Generated by Django 3.2 on 2022-03-27 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('popular', '0002_auto_20220221_2341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentlike',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='commentlike',
            name='users',
        ),
        migrations.RemoveField(
            model_name='postdislike',
            name='post',
        ),
        migrations.RemoveField(
            model_name='postdislike',
            name='users',
        ),
        migrations.RemoveField(
            model_name='postlike',
            name='post',
        ),
        migrations.RemoveField(
            model_name='postlike',
            name='users',
        ),
        migrations.DeleteModel(
            name='CommentDislike',
        ),
        migrations.DeleteModel(
            name='CommentLike',
        ),
        migrations.DeleteModel(
            name='PostDislike',
        ),
        migrations.DeleteModel(
            name='PostLike',
        ),
    ]