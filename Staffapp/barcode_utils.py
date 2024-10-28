import barcode
from barcode.writer import ImageWriter
from django.conf import settings
import os
def generate_barcode(consignment_number):
    barcode_directory = os.path.join(settings.MEDIA_ROOT, 'barcodes')
    code128 = barcode.get('code128', consignment_number, writer=ImageWriter())
    filename = code128.save(os.path.join(barcode_directory, consignment_number))  # Saves the barcode as an image
    return filename