# Generated by Django 5.0.6 on 2024-05-29 13:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=128)),
                ('ubicacion', models.CharField(max_length=128)),
                ('cant_proyector', models.IntegerField(default=0)),
                ('aforo', models.IntegerField(default=0)),
                ('es_climatizada', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=128)),
                ('apellido', models.CharField(max_length=128)),
                ('mostrar', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=128)),
                ('cant_alumnos', models.IntegerField(default=5)),
                ('id_carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aulas.carrera')),
                ('id_profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aulas.profesor')),
            ],
        ),
    ]
