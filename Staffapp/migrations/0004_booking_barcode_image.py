# Generated by Django 5.1.2 on 2024-10-28 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staffapp', '0003_remove_despatch_booking_despatch_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='barcode_image',
            field=models.ImageField(blank=True, null=True, upload_to='barcodes/'),
        ),
    ]