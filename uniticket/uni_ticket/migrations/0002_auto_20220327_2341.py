# Generated by Django 3.2.12 on 2022-03-27 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uni_ticket', '0001_squashed_0178_auto_20220326_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='code',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='input_module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='uni_ticket.ticketcategorymodule'),
        ),
    ]
