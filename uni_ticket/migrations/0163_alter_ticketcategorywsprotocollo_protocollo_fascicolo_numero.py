# Generated by Django 3.2.7 on 2021-09-24 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("uni_ticket", "0162_auto_20210924_1336"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticketcategorywsprotocollo",
            name="protocollo_fascicolo_numero",
            field=models.CharField(
                max_length=255, verbose_name="Fascicolo numero"),
        ),
    ]
