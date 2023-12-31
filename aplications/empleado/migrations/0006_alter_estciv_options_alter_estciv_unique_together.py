# Generated by Django 4.1 on 2022-10-04 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0005_estciv_empleado_estadocivil'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estciv',
            options={'ordering': ['estadocivil'], 'verbose_name': 'Estado Civil', 'verbose_name_plural': 'Estados Civiles'},
        ),
        migrations.AlterUniqueTogether(
            name='estciv',
            unique_together={('estadocivil',)},
        ),
    ]
