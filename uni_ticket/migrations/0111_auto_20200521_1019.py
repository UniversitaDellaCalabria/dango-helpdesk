# Generated by Django 3.0.6 on 2020-05-21 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("uni_ticket", "0110_auto_20200521_0926"),
    ]

    operations = [
        migrations.AddField(
            model_name="organizationalstructurewsarchipro",
            name="modified",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="ticketcategorywsarchipro",
            name="modified",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
