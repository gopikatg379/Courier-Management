# Generated by Django 5.1.2 on 2024-10-29 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staffapp', '0005_boxbarcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boxbarcode',
            name='barcode_image',
            field=models.ImageField(upload_to='box_barcodes/'),
        ),
    ]
