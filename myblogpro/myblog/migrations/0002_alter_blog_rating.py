# Generated by Django 4.2.7 on 2023-11-22 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='rating',
            field=models.BooleanField(default=False),
        ),
    ]
