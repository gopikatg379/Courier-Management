from django.db import models
from Adminapp.models import Consignor, Consignee, District, Driver, Vehicle


# Create your models here.

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    consignor = models.ForeignKey(Consignor, on_delete=models.CASCADE)
    consignee = models.ForeignKey(Consignee, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    number_of_boxes = models.IntegerField()
    status = models.CharField(max_length=12,
                              choices=[('Booked', 'Booked'), ('Delivered', 'Delivered'), ('Dispatched', 'Dispatched')],
                              default='Booked')
    date_booked = models.DateField()
    price = models.IntegerField(null=True)
    remark = models.TextField(blank=True, null=True)
    barcode_image = models.ImageField(upload_to='barcodes/', null=True, blank=True)
    class Meta:
        db_table = 'booking_table'


class Despatch(models.Model):
    despatch_id = models.AutoField(primary_key=True)
    date = models.DateField()
    booking = models.ManyToManyField(Booking)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    class Meta:
        db_table = 'despatch_table'


class Delivery(models.Model):
    delivery_id = models.AutoField(primary_key=True)
    date = models.DateField()
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    status = models.CharField(max_length=9,
                              choices=[('Pending', 'Pending'), ('Delivered', 'Delivered'), ('Return', 'Return')],
                              default='pending')

    class Meta:
        db_table = 'delivery_table'
