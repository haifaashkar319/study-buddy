# Generated by Django 4.2.4 on 2023-09-16 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FeedPages', '0002_remove_feed_id_feed_feed_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='SearchBar',
        ),
    ]