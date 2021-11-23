# Generated by Django 3.1.2 on 2020-11-27 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("uni_ticket", "0155_auto_20201127_0854"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticketcategoryinputlist",
            name="field_type",
            field=models.CharField(
                choices=[
                    ("CustomFileField", "Allegato (generico)"),
                    ("CustomImageField", "Allegato Immagine"),
                    ("CustomSignedP7MField", "Allegato P7M firmato"),
                    ("CustomPDFField", "Allegato PDF"),
                    ("CustomSignedPdfField", "Allegato PDF firmato"),
                    ("CustomDataField", "Allegato file dati (JSON, CSV, Excel)"),
                    ("CustomHiddenField", "Campo nascosto"),
                    ("CustomCaptchaComplexField", "Captcha"),
                    ("CheckBoxField", "Checkbox"),
                    ("MultiCheckBoxField", "Checkbox multi-valore"),
                    ("BaseDateField", "Data"),
                    ("BaseDateTimeField", "Data e Ora (campi separati)"),
                    ("BaseDateTimeSimpleField", "Data e ora (campo singolo)"),
                    ("DateStartEndComplexField", "Data inizio e Data fine"),
                    ("CustomEmailField", "E-mail"),
                    ("CustomIPField", "Indirizzo IP"),
                    ("CustomComplexTableField", "Inserimenti multipli"),
                    ("CustomRadioBoxField", "Lista di opzioni (checkbox)"),
                    ("CustomSelectBoxField", "Lista di opzioni (tendina)"),
                    ("CustomMACField", "MAC Address"),
                    ("PositiveFloatField", "Numero con virgola positivo"),
                    ("PositiveIntegerField", "Numero intero positivo"),
                    ("ProtocolloField", "Protocollo (tipo/numero/data)"),
                    ("CustomCharField", "Testo"),
                    ("TextAreaField", "Testo lungo"),
                    ("CustomURLField", "URL"),
                ],
                max_length=100,
            ),
        ),
    ]
