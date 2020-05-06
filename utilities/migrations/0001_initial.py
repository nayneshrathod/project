# Generated by Django 2.2.4 on 2019-12-10 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalIpdPatient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('uhidno', models.CharField(max_length=100)),
                ('listing_id', models.IntegerField()),
                ('name', models.CharField(max_length=40)),
                ('email', models.TextField(blank=True, null=True)),
                ('mlc', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('adharcard', models.CharField(blank=True, max_length=110, null=True)),
                ('phone', models.CharField(max_length=110)),
                ('relative_phoneno', models.CharField(blank=True, max_length=200, null=True)),
                ('rpname', models.CharField(blank=True, max_length=100, null=True)),
                ('relativename', models.CharField(max_length=100)),
                ('remail', models.CharField(blank=True, max_length=100, null=True)),
                ('rrelation', models.CharField(blank=True, max_length=100, null=True)),
                ('sex', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('blood_group', models.CharField(blank=True, max_length=40, null=True)),
                ('occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('mlc_no', models.IntegerField(blank=True, null=True)),
                ('state', models.CharField(blank=True, max_length=40, null=True)),
                ('city', models.CharField(blank=True, max_length=40, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('date_of_birth', models.CharField(blank=True, max_length=500, null=True)),
                ('staff_id', models.IntegerField(blank=True, null=True)),
                ('date', models.DateTimeField()),
                ('booking_type', models.IntegerField()),
                ('is_active', models.IntegerField()),
            ],
            options={
                'db_table': 'hospital_ipd_patient',
                'managed': False,
            },
        ),
    ]