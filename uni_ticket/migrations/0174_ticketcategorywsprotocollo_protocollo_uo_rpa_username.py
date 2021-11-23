# Generated by Django 3.2.7 on 2021-11-11 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("uni_ticket", "0173_auto_20211111_0923"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticketcategorywsprotocollo",
            name="protocollo_uo_rpa_username",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Username RPA sul sistema di protocollo",
                max_length=255,
                verbose_name="RPA username",
            ),
        ),
    ]
