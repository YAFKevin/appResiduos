# Generated by Django 4.1.6 on 2023-02-06 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_tipoincentivo_nombre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ruta',
            old_name='ruta',
            new_name='nombreruta',
        ),
    ]