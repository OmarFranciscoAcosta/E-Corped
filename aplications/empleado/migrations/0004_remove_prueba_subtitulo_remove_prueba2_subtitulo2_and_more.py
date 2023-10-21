# Generated by Django 4.1 on 2022-10-04 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
        ('empleado', '0003_alter_prueba2_subtitulo2_alter_prueba2_titulo2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prueba',
            name='subtitulo',
        ),
        migrations.RemoveField(
            model_name='prueba2',
            name='subtitulo2',
        ),
        migrations.AlterField(
            model_name='prueba',
            name='titulo',
            field=models.CharField(max_length=50, verbose_name='titulo'),
        ),
        migrations.AlterField(
            model_name='prueba2',
            name='titulo2',
            field=models.CharField(max_length=50, verbose_name='titulo 2'),
        ),
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades del empleado',
                'ordering': ['habilidad'],
                'unique_together': {('habilidad',)},
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, verbose_name='Nombre:')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('trabajo', models.CharField(choices=[('0', 'Contador'), ('1', 'Administrativo'), ('2', 'Desarrollador'), ('3', 'Analista Funcional'), ('4', 'Otro')], max_length=1, verbose_name='Trabajo')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.departamento')),
            ],
            options={
                'verbose_name': 'Mi empleado',
                'verbose_name_plural': 'Empleados de la empresa',
                'ordering': ['-nombre', 'apellido'],
                'unique_together': {('nombre', 'departamento')},
            },
        ),
    ]