# Generated by Django 4.1.6 on 2023-02-06 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_maquinaria_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recoleccion',
            name='observacion',
            field=models.CharField(max_length=200, null=True),
        ),
    ]