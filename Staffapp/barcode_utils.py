import barcode
from barcode.writer import ImageWriter
from django.conf import settings
import os
from barcode import Code128


def generate_main_barcode(booking_id):
    """Generate main booking barcode image."""
    barcode_directory = os.path.join(settings.MEDIA_ROOT, 'barcodes')
    os.makedirs(barcode_directory, exist_ok=True)
    filename = f'{booking_id}'
    file_path = os.path.join(barcode_directory, filename)
    code128 = Code128(str(booking_id), writer=ImageWriter())
    code128.save(file_path)
    return f'barcodes/{filename}.png'

def generate_box_barcode(booking_id, box_number):
    """Generate barcode for each box."""
    barcode_directory = os.path.join(settings.MEDIA_ROOT, 'barcodes')
    os.makedirs(barcode_directory, exist_ok=True)
    filename = f'{booking_id}-{box_number}'
    file_path = os.path.join(barcode_directory, filename)
    code128 = Code128(f"{booking_id}-{box_number}", writer=ImageWriter())
    code128.save(file_path)
    return f'barcodes/{filename}.png'