# Generated by Django 4.1 on 2022-09-21 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prueba2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo2', models.CharField(max_length=30)),
                ('subtitulo2', models.CharField(max_length=50)),
            ],
        ),
    ]
