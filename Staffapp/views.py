from django.shortcuts import render, redirect
from Adminapp.models import User, Consignor, Consignee, District, Driver, Vehicle
from Staffapp.models import Booking, Despatch
from django.contrib import messages


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
                      {'data': user_obj, 'data1': booking_obj, 'data2': driver_obj, 'data3': vehicle_obj,'data4': des_obj})
