import barcode
from barcode.writer import ImageWriter
from django.conf import settings
import os
from barcode import Code128


def generate_barcode(booking_id):
    barcode_directory = os.path.join(settings.MEDIA_ROOT, 'barcodes')
    # Construct filename with proper extension
    filename = f'{booking_id}'
    file_path = os.path.join(barcode_directory, filename)
    code128 = Code128(str(booking_id), writer=ImageWriter())
    code128.save(file_path)  # Save the barcode as an image
    return f'barcodes/{filename}.png'
