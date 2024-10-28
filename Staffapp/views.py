from django.shortcuts import render, redirect
from Adminapp.models import User, Consignor, Consignee, District, Driver, Vehicle
from Staffapp.models import Booking, Despatch, Delivery
from django.contrib import messages
from .barcode_utils import generate_barcode

# Create your views here.


def add_booking(request):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        if request.method == 'POST':
            booking_obj = Booking()
            booking_obj.date_booked = request.POST.get('date')
            try:
                consignor_obj = Consignor.objects.get(consignor_id=request.POST.get('consignor'))
                booking_obj.consignor = consignor_obj
            except Consignor.DoesNotExist:
                messages.error(request, 'Invalid consignor selected')
                return redirect('/staff/add_booking')
            try:
                consignee_obj = Consignee.objects.get(consignee_id=request.POST.get('consignee'))
                booking_obj.consignee = consignee_obj
            except Consignee.DoesNotExist:
                messages.error(request, 'Invalid consignee selected')
                return redirect('/staff/add_booking')
            try:
                district_obj = District.objects.get(district_id=request.POST.get('district'))
                booking_obj.district = district_obj
            except District.DoesNotExist:
                messages.error(request, 'Invalid district selected')
                return redirect('/staff/add_booking')
            booking_obj.number_of_boxes = request.POST.get('number')
            booking_obj.weight = request.POST.get('weight')
            booking_obj.price = request.POST.get('price')
            booking_obj.remark = request.POST.get('remark')
            booking_obj.save()
            barcode_filename = generate_barcode(str(booking_obj.booking_id))
            booking_obj.barcode_image = barcode_filename
            booking_obj.save(update_fields=['barcode_image'])
            messages.success(request, 'Booking added successfully!')
            return redirect('/staff/add_booking')
        con_obj = Consignor.objects.all()
        cons_obj = Consignee.objects.all()
        dis_obj = District.objects.all()
        return render(request, 'add_booking.html',
                      {'data': user_obj, 'data1': con_obj, 'data2': cons_obj, 'data3': dis_obj})
    else:
        return redirect('/')


def edit_booking(request, booking_id):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        booking_obj = Booking.objects.get(booking_id=booking_id)
        if request.method == 'POST':
            booking_obj = Booking.objects.get(booking_id=booking_id)
            booking_obj.date_booked = request.POST.get('date')
            try:
                consignor_obj = Consignor.objects.get(consignor_id=request.POST.get('consignor'))
                booking_obj.consignor = consignor_obj
            except Consignor.DoesNotExist:
                messages.error(request, 'Invalid consignor selected')
                return redirect('/list_booking')
            try:
                consignee_obj = Consignee.objects.get(consignee_id=request.POST.get('consignee'))
                booking_obj.consignee = consignee_obj
            except Consignee.DoesNotExist:
                messages.error(request, 'Invalid consignee selected')
                return redirect('/list_booking')
            try:
                district_obj = District.objects.get(district_id=request.POST.get('district'))
                booking_obj.district = district_obj
            except District.DoesNotExist:
                messages.error(request, 'Invalid district selected')
                return redirect('/list_booking')
            booking_obj.number_of_boxes = request.POST.get('number')
            booking_obj.weight = request.POST.get('weight')
            booking_obj.price = request.POST.get('price')
            booking_obj.remark = request.POST.get('remark')
            booking_obj.save()

            messages.success(request, 'Booking updated successfully!')
            return redirect('/list_booking')
        con_obj = Consignor.objects.all()
        cons_obj = Consignee.objects.all()
        dis_obj = District.objects.all()
        return render(request, 'edit_booking.html',
                      {'data': user_obj, 'data1': booking_obj, 'data2': con_obj, 'data3': cons_obj, 'data4': dis_obj})
    else:
        return redirect('/')


def add_despatch(request):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        if request.method == 'POST':
            despatch_obj = Despatch()
            despatch_obj.date = request.POST.get('date')
            despatch_obj.driver = Driver.objects.get(driver_id=request.POST.get('driver'))
            despatch_obj.vehicle = Vehicle.objects.get(vehicle_id=request.POST.get('vehicle'))
            despatch_obj.save()
            selected_bookings = request.POST.getlist('booking')
            for booking_id in selected_bookings:
                booking = Booking.objects.get(booking_id=booking_id)
                despatch_obj.booking.add(booking)
            despatch_obj.save()
            messages.success(request, 'Despatch added successfully!')
            return redirect('/staff/add_despatch')
        booking_obj = Booking.objects.filter(despatch__isnull=True)
        driver_obj = Driver.objects.all()
        vehicle_obj = Vehicle.objects.all()
        des_obj = Despatch.objects.all()
        return render(request, 'add_despatch.html',
                      {'data': user_obj, 'data1': booking_obj, 'data2': driver_obj, 'data3': vehicle_obj,
                       'data4': des_obj})


def add_delivery(request):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        booking_obj = Booking.objects.all()
        print(booking_obj)
        if request.method == 'POST':
            search = request.POST.get('booking_id')
            if search:
                booking_obj = booking_obj.filter(booking_id__icontains=search)
                print(booking_obj)
                delivery_obj = Delivery()
                delivery_obj.date = request.POST.get('date')
                delivery_obj.booking = Booking.objects.get(booking_id=request.POST.get('booking_id'))
                dels_status = request.POST.get('del_status')
                ret_status = request.POST.get('ret_status')
                if dels_status:
                    delivery_obj.status = 'delivered'
                elif ret_status:
                    delivery_obj.status = 'returned'
                delivery_obj.save()
                messages.success(request, 'Delivery added successfully!')
        delivered_or_returned_ids = Delivery.objects.filter(status__in=['delivered', 'returned']).values_list(
            'booking_id', flat=True)
        booking_obj = Booking.objects.exclude(booking_id__in=delivered_or_returned_ids)
        delivery_obj = Delivery.objects.all()
        print(delivery_obj)
        return render(request, 'add_delivery.html', {'data': user_obj, 'data1': booking_obj, 'data2': delivery_obj})
    else:
        return redirect('/')
