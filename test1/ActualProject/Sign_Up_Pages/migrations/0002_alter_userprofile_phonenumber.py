# Generated by Django 4.2.4 on 2023-09-09 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sign_Up_Pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='PhoneNumber',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=65),
        ),
    ]
