# Generated by Django 4.2.7 on 2023-11-30 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0003_sport_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sport",
            name="content",
        ),
        migrations.RemoveField(
            model_name="sport",
            name="title",
        ),
        migrations.AddField(
            model_name="sport",
            name="category",
            field=models.CharField(
                choices=[
                    ("Athletics", "Athletics"),
                    ("Team sport", "Team Sport"),
                    ("Individual sport", "Individual Sport"),
                    ("Water sport", "Water Sport"),
                    ("Skiing sport", "Skiing Sport"),
                ],
                default="Athletics",
                max_length=64,
            ),
        ),
        migrations.AddField(
            model_name="sport",
            name="description",
            field=models.TextField(default="fffffff"),
        ),
        migrations.AddField(
            model_name="sport",
            name="name",
            field=models.CharField(default="fffffff", max_length=1024),
        ),
        migrations.AddField(
            model_name="sport",
            name="rating",
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
