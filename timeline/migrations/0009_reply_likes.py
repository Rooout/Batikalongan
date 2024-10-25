# Generated by Django 5.1.2 on 2024-10-26 12:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0008_likedreply'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='likes',
            field=models.ManyToManyField(related_name='likedreplies', through='timeline.LikedReply', to=settings.AUTH_USER_MODEL),
        ),
    ]
