# Generated by Django 4.0.6 on 2022-08-07 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datcarta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datcarta',
            name='Fecha_de_Ingreso',
            field=models.DateField(auto_now_add=True),
        ),
    ]
