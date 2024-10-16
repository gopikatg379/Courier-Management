from django.db import models


# Create your models here.

class Designation(models.Model):
    designation_id = models.AutoField(primary_key=True)
    designation = models.CharField(max_length=200)

    class Meta:
        db_table = 'designation_table'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=16)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    user_status = models.CharField(max_length=8, choices=[('Active', 'Active'), ('Inactive', 'Inactive')],
                                   default='Active')

    class Meta:
        db_table = 'user_table'


class Consignee(models.Model):
    consignee_id = models.AutoField(primary_key=True)
    consignee_name = models.CharField(max_length=255)
    consignee_phone = models.CharField(max_length=12)
    consignee_address = models.CharField(max_length=255)
    consignee_status = models.CharField(max_length=8, choices=[('Active', 'Active'), ('Inactive', 'Inactive')],
                                        default='Active')

    class Meta:
        db_table = 'consignee_table'


class Consignor(models.Model):
    consignor_id = models.AutoField(primary_key=True)
    consignor_name = models.CharField(max_length=255)
    consignor_phone = models.CharField(max_length=12)
    consignor_address = models.CharField(max_length=255)
    consignor_status = models.CharField(max_length=8, choices=[('Active', 'Active'), ('Inactive', 'Inactive')],
                                        default='Active')

    class Meta:
        db_table = 'consignor_table'


class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    driver_name = models.CharField(max_length=255)
    driver_phone = models.CharField(max_length=12)
    driver_address = models.CharField(max_length=255)
    driver_status = models.CharField(max_length=8, choices=[('Active', 'Active'), ('Inactive', 'Inactive')],
                                     default='Active')

    class Meta:
        db_table = 'driver_table'


class District(models.Model):
    district_id = models.AutoField(primary_key=True)
    district_name = models.CharField(max_length=255)
    state = models.CharField(max_length=200)
    district_status = models.CharField(max_length=8, choices=[('Active', 'Active'), ('Inactive', 'Inactive')],
                                       default='Active')

    class Meta:
        db_table = 'district_table'


class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    vehicle_name = models.CharField(max_length=255)
    vehicle_number = models.CharField(max_length=12)
    vehicle_status = models.CharField(max_length=8, choices=[('Active', 'Active'), ('Inactive', 'Inactive')],
                                      default='Active')

    class Meta:
        db_table = 'vehicle_table'
