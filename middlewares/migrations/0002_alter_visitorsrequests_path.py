# Generated by Django 4.1.3 on 2022-12-09 19:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("middlewares", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="visitorsrequests",
            name="path",
            field=models.SlugField(max_length=255),
        ),
    ]
