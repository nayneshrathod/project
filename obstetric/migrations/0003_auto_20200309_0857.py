# Generated by Django 2.2.4 on 2020-03-09 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obstetric', '0002_auto_20200309_0839'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='obstetricform',
            table='obstetric_form',
        ),
        migrations.AlterModelTable(
            name='obstetricphysicalexamination',
            table='obstetric_physical_examination',
        ),
    ]