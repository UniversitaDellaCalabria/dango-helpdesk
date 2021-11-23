# Generated by Django 3.0.6 on 2020-05-27 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("uni_ticket", "0118_auto_20200522_1318"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticketcategory",
            name="confirm_message_text",
            field=models.TextField(
                blank=True,
                help_text='Es: \'Hai correttamente confermato la tua partecipazione\'. Apri e chiudi le parentesi graffe per inserire l\'oggetto del ticket. Lascia vuoto per usare il testo predefinito "Ticket "{}" creato con successo"',
                max_length=500,
                null=True,
                verbose_name="Messaggio di conferma",
            ),
        ),
    ]
