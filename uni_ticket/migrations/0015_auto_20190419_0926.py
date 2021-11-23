# Generated by Django 2.1.7 on 2019-04-19 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("uni_ticket", "0014_auto_20190418_0849"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticketcategory",
            name="modified",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="ticketcategoryinputlist",
            name="input_type",
            field=models.CharField(
                choices=[
                    ("CustomFileField", "Allegato PDF"),
                    ("CustomHiddenField", "Campo nascosto"),
                    ("CheckBoxField", "Checkbox"),
                    ("BaseDateField", "Data"),
                    ("BaseDateTimeField", "Data e Ora"),
                    ("DateStartEndComplexField", "Data inizio e Data fine"),
                    (
                        "DurataComeInteroField",
                        "Durata come numero intero (anni,mesi,ore)",
                    ),
                    ("CustomListField", "Lista di campi testuali"),
                    ("CustomRadioBoxField", "Lista di opzioni (checkbox)"),
                    ("CustomSelectBoxField", "Lista di opzioni (tendina)"),
                    ("PositiveFloatField", "Numero con virgola positivo"),
                    ("PositiveIntegerField", "Numero intero positivo"),
                    ("ProtocolloField", "Protocollo (tipo/numero/data)"),
                    ("CustomCharField", "Testo"),
                    ("TextAreaField", "Testo lungo"),
                ],
                max_length=33,
            ),
        ),
    ]
