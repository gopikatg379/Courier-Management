# Generated by Django 5.1.2 on 2024-10-14 05:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consignee',
            fields=[
                ('consignee_id', models.AutoField(primary_key=True, serialize=False)),
                ('consignee_name', models.CharField(max_length=255)),
                ('consignee_phone', models.CharField(max_length=12)),
                ('consignee_address', models.CharField(max_length=255)),
                ('consignee_status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=8)),
            ],
            options={
                'db_table': 'consignee_table',
            },
        ),
        migrations.CreateModel(
            name='Consignor',
            fields=[
                ('consignor_id', models.AutoField(primary_key=True, serialize=False)),
                ('consignor_name', models.CharField(max_length=255)),
                ('consignor_phone', models.CharField(max_length=12)),
                ('consignor_address', models.CharField(max_length=255)),
                ('consignor_status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=8)),
            ],
            options={
                'db_table': 'consignor_table',
            },
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('designation_id', models.AutoField(primary_key=True, serialize=False)),
                ('designation', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'designation_table',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('district_id', models.AutoField(primary_key=True, serialize=False)),
                ('district_name', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=200)),
                ('district_status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=8)),
            ],
            options={
                'db_table': 'district_table',
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('driver_id', models.AutoField(primary_key=True, serialize=False)),
                ('driver_name', models.CharField(max_length=255)),
                ('driver_phone', models.CharField(max_length=12)),
                ('driver_address', models.CharField(max_length=255)),
                ('driver_status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=8)),
            ],
            options={
                'db_table': 'driver_table',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_id', models.AutoField(primary_key=True, serialize=False)),
                ('vehicle_name', models.CharField(max_length=255)),
                ('vehicle_number', models.CharField(max_length=12)),
                ('vehicle_status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=8)),
            ],
            options={
                'db_table': 'vehicle_table',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=12)),
                ('user_status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=8)),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Adminapp.designation')),
            ],
            options={
                'db_table': 'user_table',
            },
        ),
    ]
