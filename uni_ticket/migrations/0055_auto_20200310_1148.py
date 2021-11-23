# Generated by Django 3.0.3 on 2020-03-10 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("uni_ticket", "0054_delete_taskhistory"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticketcategoryinputlist",
            name="field_type",
            field=models.CharField(
                choices=[
                    ("CustomSignedP7MField", "Allegato P7M firmato"),
                    ("CustomFileField", "Allegato PDF"),
                    ("CustomSignedPdfField", "Allegato PDF firmato"),
                    ("CustomHiddenField", "Campo nascosto"),
                    ("CheckBoxField", "Checkbox"),
                    ("BaseDateField", "Data"),
                    ("BaseDateTimeField", "Data e Ora"),
                    ("DateStartEndComplexField", "Data inizio e Data fine"),
                    ("CustomEmailField", "E-mail"),
                    ("CustomComplexTableField", "Inserimenti multipli"),
                    ("CustomRadioBoxField", "Lista di opzioni (checkbox)"),
                    ("CustomSelectBoxField", "Lista di opzioni (tendina)"),
                    ("PositiveFloatField", "Numero con virgola positivo"),
                    ("PositiveIntegerField", "Numero intero positivo"),
                    ("ProtocolloField", "Protocollo (tipo/numero/data)"),
                    ("CustomCharField", "Testo"),
                    ("TextAreaField", "Testo lungo"),
                ],
                max_length=100,
            ),
        ),
    ]
