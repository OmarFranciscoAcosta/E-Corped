# Generated by Django 4.1 on 2022-10-04 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0006_alter_estciv_options_alter_estciv_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='estadocivil',
            new_name='Situacion',
        ),
    ]