# Generated by Django 4.1.6 on 2023-02-06 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_recoleccion_observacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recoleccion',
            name='observacion',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
