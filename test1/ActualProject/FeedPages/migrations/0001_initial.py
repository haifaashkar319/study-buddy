# Generated by Django 4.2.4 on 2023-09-16 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SearchBar', models.CharField(default='none', max_length=200)),
                ('Feed_Owner', models.IntegerField(max_length=255)),
                ('Description', models.CharField(default='none', max_length=255)),
                ('Knowledge', models.IntegerField(max_length=255)),
                ('course', models.IntegerField(max_length=255)),
            ],
            options={
                'db_table': 'feedtable',
            },
        ),
    ]
