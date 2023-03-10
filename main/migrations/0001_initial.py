# Generated by Django 4.1.5 on 2023-02-06 04:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ciudadano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('documento', models.CharField(max_length=20, unique=True)),
                ('celular', models.CharField(max_length=9, unique=True)),
                ('direccion', models.CharField(max_length=100)),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='empadronamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='maquinaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('placa', models.CharField(max_length=7, unique=True)),
                ('estado', models.BooleanField()),
                ('cargaNeta', models.FloatField()),
                ('cargaUtil', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('documento', models.CharField(max_length=20, unique=True)),
                ('fechaNacimiento', models.DateField()),
                ('correo', models.CharField(max_length=100, unique=True)),
                ('celular', models.CharField(max_length=9, unique=True)),
                ('direccion', models.CharField(max_length=100)),
                ('estado', models.BooleanField()),
                ('idEmpadro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.empadronamiento')),
            ],
        ),
        migrations.CreateModel(
            name='residuo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, unique=True)),
                ('descripcion', models.TextField(blank=True)),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='tipoCiudadano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='tipoDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='tipoIncentivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='tipoMaquinaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='tipoPersonal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='tipoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField(blank=True)),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='zona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ruta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruta', models.CharField(max_length=200)),
                ('lugarInicio', models.CharField(max_length=100)),
                ('lugarFin', models.CharField(max_length=100)),
                ('idZona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.zona')),
            ],
        ),
        migrations.CreateModel(
            name='recoleccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacion', models.CharField(max_length=200)),
                ('Horario_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.horario')),
                ('Maquinaria_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.maquinaria')),
                ('Personal_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.personal')),
                ('Residuo_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.residuo')),
                ('Usuario_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='personal',
            name='idTipoDoc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tipodocumento'),
        ),
        migrations.AddField(
            model_name='personal',
            name='idTipoPersonal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tipopersonal'),
        ),
        migrations.AddField(
            model_name='maquinaria',
            name='idTipoMaqui',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tipomaquinaria'),
        ),
        migrations.AddField(
            model_name='horario',
            name='idRuta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ruta'),
        ),
        migrations.CreateModel(
            name='detalleIncentivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('idCiudadano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ciudadano')),
                ('idRecoleccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.recoleccion')),
                ('idTipoIncentivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tipoincentivo')),
            ],
        ),
        migrations.AddField(
            model_name='ciudadano',
            name='idEmpadro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.empadronamiento'),
        ),
        migrations.AddField(
            model_name='ciudadano',
            name='idTipoCiud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tipociudadano'),
        ),
        migrations.AddField(
            model_name='ciudadano',
            name='idTipoDoc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tipodocumento'),
        ),
    ]
