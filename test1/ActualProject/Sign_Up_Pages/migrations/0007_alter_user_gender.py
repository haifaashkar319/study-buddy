# Generated by Django 4.2.4 on 2023-09-19 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sign_Up_Pages', '0006_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Gender',
            field=models.TextField(default='none'),
        ),
    ]