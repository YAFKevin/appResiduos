# Generated by Django 4.1.5 on 2023-02-26 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_medidarecoleccion_recoleccion_peso_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudadano',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='maquinaria',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='zona',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]
