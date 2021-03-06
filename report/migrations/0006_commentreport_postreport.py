# Generated by Django 3.2 on 2022-03-27 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exhibition', '0018_alter_post_artform'),
        ('comments', '0003_alter_comment_user_name'),
        ('report', '0005_auto_20220327_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('reason', models.IntegerField(choices=[(0, 'Explicit Content'), (1, 'Inappropriate Image'), (2, 'Profanity'), (3, 'Offensive'), (4, 'Violence'), (5, 'Bullying'), (6, 'Harassment')], default=0)),
                ('more_info', models.TextField(blank=True, max_length=300)),
                ('reported_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_post', to='exhibition.post')),
                ('reporting_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('reason', models.IntegerField(choices=[(0, 'Explicit Content'), (1, 'Inappropriate Image'), (2, 'Profanity'), (3, 'Offensive'), (4, 'Violence'), (5, 'Bullying'), (6, 'Harassment')], default=0)),
                ('more_info', models.TextField(blank=True, max_length=300)),
                ('reported_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_comment', to='comments.comment')),
                ('reporting_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
