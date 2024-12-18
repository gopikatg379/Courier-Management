from django.shortcuts import render, redirect
from .models import Designation, User, Consignor, Consignee, District, Driver, Vehicle
from django.contrib import messages
from Staffapp.models import Booking, Despatch, Delivery, BoxBarcode
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.

def add_designation(request):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        if request.method == 'POST':
            des_obj = Designation()
            des_obj.designation = request.POST.get('designation_name')
            des_obj.save()
            messages.success(request, 'Designation added successfully!')
            return redirect('/add_designation')
        return render(request, 'designation.html', {'data': user_obj})
    else:
        return redirect('/')


def list_designation(request):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        des_obj = Designation.objects.all()
        if request.method == 'POST':
            search = request.POST.get('designation')
            if search:
                des_obj = des_obj.filter(designation__icontains=search)
        return render(request, 'list_designation.html', {'data1': des_obj, 'data': user_obj})
    else:
        return redirect('/')


def add_user(request):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        if request.method == 'POST':
            user_obj = User()
            user_obj.username = request.POST.get('username')
            user_obj.email = request.POST.get('email')
            user_obj.password = request.POST.get('password')
            user_obj.phone_number = request.POST.get('phone_number')
            try:
                des_obj = Designation.objects.get(designation_id=request.POST.get('designation'))
                user_obj.designation = des_obj
            except Designation.DoesNotExist:
                return redirect('/add_designation')
            user_obj.user_status = request.POST.get('user_status')
            if user_obj.user_status is None:
                user_obj.user_status = 'inactive'
            elif user_obj.user_status == 'on':
                user_obj.user_status = 'active'
            user_obj.save()
            return redirect('/add_user')
        des_obj = Designation.objects.all()
        return render(request, 'add_user.html', {'data1': des_obj, 'data': user_obj})
    else:
        return redirect('/')


def list_user(request):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        user_data = User.objects.all()
        if request.method == 'POST':
            search = request.POST.get('username')
            if search:
                user_data = user_data.filter(username__icontains=search)
        return render(request, 'list_user.html', {'data1': user_data, 'data': user_obj})
    else:
        return redirect('/')


def delete_user(request, user_id):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=user_id)
        user_obj.delete()
        messages.success(request, 'User deleted successfully')
        return redirect('/list_user')
    else:
        return redirect('/')


def edit_user(request, user_id):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=user_id)
        if request.method == 'POST':
            user_obj.username = request.POST.get('username')
            try:
                des_obj = Designation.objects.get(designation_id=request.POST.get('designation'))
                user_obj.designation = des_obj
            except Designation.DoesNotExist:
                return redirect('/add_designation')
            user_obj.email = request.POST.get('email')
            user_obj.phone_number = request.POST.get('phone_number')
            user_obj.password = request.POST.get('password')
            user_obj.user_status = request.POST.get('user_status')
            user_obj.save()
            return redirect('/list_user')
        des_obj = Designation.objects.all()
        return render(request, 'edit_user.html', {'data': user_obj, 'data1': des_obj})
    else:
        return redirect('/')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user_obj = User.objects.get(username=username, password=password)
            if user_obj.user_status == 'active' and user_obj.designation.designation == 'Staff':
                request.session['user_id'] = user_obj.user_id
                request.session['username'] = user_obj.username
                return redirect('/dashboard')
            elif user_obj.user_status == 'active' and user_obj.designation.designation == 'Admin':
                request.session['user_id'] = user_obj.user_id
                request.session['username'] = user_obj.username
                return redirect('/dashboard')
            else:
                messages.error(request, 'User is inactive')
                return render(request, 'login.html')
        except User.DoesNotExist:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')
    return render(request, 'login.html')


def dashboard(request):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        return render(request, 'dashboard.html', {'data': user_obj})
    else:
        return redirect('/')


# def staff_dashboard(request):
#     if 'user_id' in request.session:
#         user_obj = User.objects.get(user_id=request.session['user_id'])
#         return render(request, 'staff_dashboard.html', {'data': user_obj})
#     else:
#         return redirect('/')


def signout(request):
    return redirect('/')


def add_consignor(request):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        if request.method == 'POST':
            con_obj = Consignor()
            con_obj.consignor_name = request.POST.get('consignor_name')
            con_obj.consignor_phone = request.POST.get('consignor_phone')
            con_obj.consignor_address = request.POST.get('consignor_address')
            con_obj.consignor_status = request.POST.get('consignor_status')
            if con_obj.consignor_status is None:
                con_obj.consignor_status = 'inactive'
            elif con_obj.consignor_status == 'on':
                con_obj.consignor_status = 'active'
            con_obj.save()
            messages.success(request, 'Consignor added successfully!')
            return redirect('/add_consignor')
    else:
        return redirect('/')
    return render(request, 'add_consignor.html', {'data': user_obj})


def list_consignor(request):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        list_obj = Consignor.objects.all()
        if request.method == 'POST':
            search = request.POST.get('consignor_name')
            if search:
                list_obj = list_obj.filter(consignor_name__icontains=search)
        return render(request, 'list_consignor.html', {'data1': list_obj, 'data': user_obj})
    else:
        return redirect('/')


def delete_consignor(request, consignor_id):
    con_obj = Consignor.objects.get(consignor_id=consignor_id)
    con_obj.delete()
    messages.success(request, 'Consignor deleted successfully!')
    return redirect('/list_consignor')


def edit_consignor(request, consignor_id):
    con_obj = Consignor.objects.get(consignor_id=consignor_id)
    if request.method == 'POST':
        con_obj = Consignor.objects.get(consignor_id=consignor_id)
        con_obj.consignor_name = request.POST.get('consignor_name')
        con_obj.consignor_phone = request.POST.get('consignor_phone')
        con_obj.consignor_address = request.POST.get('consignor_address')
        con_obj.consignor_status = request.POST.get('consignor_status')
        if con_obj.consignor_status is None:
            con_obj.consignor_status = 'inactive'
        elif con_obj.consignor_status == 'on':
            con_obj.consignor_status = 'active'
        con_obj.save()
        return redirect('/list_consignor')
    return render(request, 'edit_consignor.html', {'data': con_obj})


def delete_designation(request, designation_id):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        des_obj = Designation.objects.get(designation_id=designation_id)
        des_obj.delete()
        messages.success(request, 'Designation deleted successfully')
        return redirect('/list_designation')
    else:
        return redirect('/')


def edit_designation(request, designation_id):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        des_obj = Designation.objects.get(designation_id=designation_id)
        if request.method == 'POST':
            des_obj = Designation.objects.get(designation_id=designation_id)
            des_obj.designation = request.POST.get('designation')
            des_obj.save()
            messages.success(request, 'Designation updated successfully!')
            return redirect('/list_designation')
        return render(request, 'edit_designation.html', {'data1': des_obj, 'data': user_obj})
    else:
        return redirect('/')


def add_consignee(request):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        if request.method == 'POST':
            con_obj = Consignee()
            con_obj.consignee_name = request.POST.get('consignee_name')
            con_obj.consignee_phone = request.POST.get('consignee_phone')
            con_obj.consignee_address = request.POST.get('consignee_address')
            con_obj.consignee_status = request.POST.get('consignee_status')
            if con_obj.consignee_status is None:
                con_obj.consignee_status = 'inactive'
            elif con_obj.consignee_status == 'on':
                con_obj.consignee_status = 'active'
            con_obj.save()
            messages.success(request, 'Consignee added successfully!')
            return redirect('/add_consignee')
        return render(request, 'add_consignee.html', {'data': user_obj})


def list_consignee(request):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        list_obj = Consignee.objects.all()
        if request.method == 'POST':
            search = request.POST.get('consignee_name')
            if search:
                list_obj = list_obj.filter(consignee_name__icontains=search)
        return render(request, 'list_consignee.html', {'data1': list_obj, 'data': user_obj})
    else:
        return redirect('/')


def delete_consignee(request, consignee_id):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        con_obj = Consignee.objects.get(consignee_id=consignee_id)
        con_obj.delete()
        messages.success(request, 'Consignee deleted successfully!')
        return redirect('/list_consignee')
    else:
        return redirect('/')


def edit_consignee(request, consignee_id):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        con_obj = Consignee.objects.get(consignee_id=consignee_id)
        if request.method == 'POST':
            con_obj = Consignee.objects.get(consignee_id=consignee_id)
            con_obj.consignee_name = request.POST.get('consignee_name')
            con_obj.consignee_phone = request.POST.get('consignee_phone')
            con_obj.consignee_address = request.POST.get('consignee_address')
            con_obj.consignee_status = request.POST.get('consignee_status')
            if con_obj.consignee_status is None:
                con_obj.consignee_status = 'inactive'
            elif con_obj.consignee_status == 'on':
                con_obj.consignee_status = 'active'
            con_obj.save()
            messages.success(request, "Consignee Updated successfully")
            return redirect('/list_consignee')
        return render(request, 'edit_consignee.html', {'data1': con_obj, 'data': user_obj})


def add_district(request):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        if request.method == 'POST':
            dis_obj = District()
            dis_obj.district_name = request.POST.get('district_name')
            dis_obj.state = request.POST.get('state')
            dis_obj.save()
            messages.success(request, 'District added successfully!')
            return redirect('/add_district')
        return render(request, 'add_district.html', {'data': user_obj})


def list_districts(request):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        dis_obj = District.objects.all()
        if request.method == 'POST':
            search = request.POST.get('district_name')
            if search:
                dis_obj = dis_obj.filter(district_name__icontains=search)
        return render(request, 'list_districts.html', {'data1': dis_obj, 'data': user_obj})
    else:
        return redirect('/')


def delete_district(request, district_id):
    if 'user_id' in request.session:
        dis_obj = District.objects.get(district_id=district_id)
        dis_obj.delete()
        messages.success(request, 'District deleted successfully')
        return redirect('/list_district')
    else:
        return redirect('/')


def edit_district(request, district_id):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        dis_obj = District.objects.get(district_id=district_id)
        if request.method == 'POST':
            dis_obj = District.objects.get(district_id=district_id)
            dis_obj.district_name = request.POST.get('district_name')
            dis_obj.state = request.POST.get('state')
            dis_obj.save()
            messages.success(request, 'District updated successfully!')
            return redirect('/list_district')
        return render(request, 'edit_district.html', {'data1': dis_obj, 'data': user_obj})


def add_driver(request):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        if request.method == 'POST':
            dr_obj = Driver()
            dr_obj.driver_name = request.POST.get('driver_name')
            dr_obj.driver_phone = request.POST.get('driver_phone')
            dr_obj.driver_address = request.POST.get('driver_address')
            dr_obj.save()
            messages.success(request, 'Driver added successfully!')
            return redirect('/add_driver')
        return render(request, 'add_driver.html', {'data': user_obj})


def list_drivers(request):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        dr_obj = Driver.objects.all()
        if request.method == 'POST':
            search = request.POST.get('driver_name')
            if search:
                dr_obj = dr_obj.filter(driver_name__icontains=search)
        return render(request, 'list_driver.html', {'data1': dr_obj, 'data': user_obj})
    else:
        return redirect('/')


def delete_driver(request, driver_id):
    if 'user_id' in request.session:
        dr_obj = Driver.objects.get(driver_id=driver_id)
        dr_obj.delete()
        messages.success(request, 'Driver deleted successfully!')
        return redirect('/list_driver')
    else:
        return redirect('/')


def edit_driver(request, driver_id):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        dr_obj = Driver.objects.get(driver_id=driver_id)
        if request.method == 'POST':
            dr_obj = Driver.objects.get(driver_id=driver_id)
            dr_obj.driver_name = request.POST.get('driver_name')
            dr_obj.driver_phone = request.POST.get('driver_phone')
            dr_obj.driver_address = request.POST.get('driver_address')
            dr_obj.save()
            messages.success(request, 'Driver updated successfully!')
            return redirect('/list_driver')
        return render(request, 'edit_driver.html', {'data1': dr_obj, 'data': user_obj})


def add_vehicle(request):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        if request.method == 'POST':
            ve_obj = Vehicle()
            ve_obj.vehicle_name = request.POST.get('vehicle_name')
            ve_obj.vehicle_number = request.POST.get('vehicle_number')
            ve_obj.vehicle_status = request.POST.get('vehicle_status')
            if ve_obj.vehicle_status is None:
                ve_obj.vehicle_status = 'inactive'
            elif ve_obj.vehicle_status == 'on':
                ve_obj.vehicle_status = 'active'
            ve_obj.save()
            return redirect('/add_vehicle')
        return render(request, 'add_vehicle.html', {'data': user_obj})


def list_vehicle(request):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        ve_obj = Vehicle.objects.all()
        if request.method == 'POST':
            search = request.POST.get('vehicle_name')
            if search:
                ve_obj = ve_obj.filter(vehicle_name__icontains=search)
        return render(request, 'list_vehicle.html', {'data1': ve_obj, 'data': user_obj})
    else:
        return redirect('/')


def delete_vehicle(request, vehicle_id):
    if 'user_id' in request.session:
        ve_obj = Vehicle.objects.get(vehicle_id=vehicle_id)
        ve_obj.delete()
        messages.success(request, 'Vehicle deleted successfully!')
        return redirect('/list_vehicle')
    else:
        return redirect('/')


def edit_vehicle(request, vehicle_id):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        ve_obj = Vehicle.objects.get(vehicle_id=vehicle_id)
        if request.method == 'POST':
            ve_obj = Vehicle.objects.get(vehicle_id=vehicle_id)
            ve_obj.vehicle_name = request.POST.get('vehicle_name')
            ve_obj.vehicle_number = request.POST.get('vehicle_number')
            ve_obj.vehicle_status = request.POST.get('vehicle_status')
            if ve_obj.vehicle_status is None:
                ve_obj.vehicle_status = 'inactive'
            elif ve_obj.vehicle_status == 'on':
                ve_obj.vehicle_status = 'active'
            ve_obj.save()
            messages.success(request, 'Vehicle details updated')
            return redirect('/list_vehicle')
        return render(request, 'edit_vehicle.html', {'data1': ve_obj, 'data': user_obj})


def list_booking(request):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        booking_obj = Booking.objects.all()

        # Search functionality
        if request.method == 'POST':
            search = request.POST.get('search')
            if search:
                booking_obj = booking_obj.filter(Q(booking_id__icontains=search))

        # Pagination setup
        paginator = Paginator(booking_obj, 10)  # Show 10 bookings per page
        page_number = request.GET.get('page')

        try:
            page_obj = paginator.get_page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.get_page(1)
        except EmptyPage:
            page_obj = paginator.get_page(paginator.num_pages)

        return render(request, 'list_booking.html', {'data1': page_obj, 'data': user_obj})
    else:
        return redirect('/')



def delete_booking(request, booking_id):
    if 'user_id' in request.session:
        booking_obj = Booking.objects.get(booking_id=booking_id)
        booking_obj.delete()
        messages.success(request, 'Booking deleted successfully!')
        return redirect('/list_booking')
    else:
        return redirect('/')


def list_despatch(request):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        despatch_obj = Despatch.objects.all()

        # Search functionality
        if request.method == 'POST':
            search = request.POST.get('search')
            if search:
                despatch_obj = despatch_obj.filter(despatch_number__icontains=search)

        # Pagination setup
        paginator = Paginator(despatch_obj, 10)  # Show 10 despatch items per page
        page_number = request.GET.get('page')

        try:
            page_obj = paginator.get_page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.get_page(1)
        except EmptyPage:
            page_obj = paginator.get_page(paginator.num_pages)

        return render(request, 'list_despatch.html', {'data1': page_obj, 'data': user_obj})
    else:
        return redirect('/')


def despatch_list(request, despatch_id):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        try:
            # Fetch the despatch object and related bookings
            despatch_obj = Despatch.objects.prefetch_related('booking__consignor', 'booking__consignee').get(
                despatch_id=despatch_id)
        except Despatch.DoesNotExist:
            despatch_obj = None
            bookings = []
        else:
            bookings = despatch_obj.booking.all()

        booking_data = []
        if despatch_obj:
            for booking in bookings:
                booking_data.append({
                    'booking_id': booking.booking_id,
                    'consignor_name': booking.consignor.consignor_name,
                    'consignee_name': booking.consignee.consignee_name,
                    'weight': booking.weight,
                    'price': booking.price,
                    'number_of_boxes': booking.number_of_boxes
                })

        # Pagination setup
        paginator = Paginator(booking_data, 10)  # Show 10 bookings per page
        page_number = request.GET.get('page')

        try:
            page_obj = paginator.get_page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.get_page(1)
        except EmptyPage:
            page_obj = paginator.get_page(paginator.num_pages)

        # Handle search functionality
        if request.method == 'POST':
            search = request.POST.get('search')
            if search:
                page_obj = [booking for booking in booking_data if search in booking['booking_id']]

        return render(request, 'despatch_list.html', {'data1': page_obj, 'data': user_obj, 'data2': despatch_obj})
    else:
        return redirect('/')


def delete_despatch(request, despatch_id):
    if 'user_id' in request.session:
        despatch_obj = Despatch.objects.get(despatch_id=despatch_id)
        despatch_obj.delete()
        messages.success(request, 'Despatch deleted successfully!')
        return redirect('/list_despatch')
    else:
        return redirect('/')


def list_delivery(request):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        del_obj = Delivery.objects.filter(Q(status__icontains='Delivered') | Q(status__icontains='Returned'))
        return render(request, 'list_delivery.html', {'data1': del_obj, 'data': user_obj})
    else:
        return redirect('/')


def pod_details(request, booking_id):
    if 'user_id' in request.session:
        user_obj = User.objects.get(user_id=request.session['user_id'])
        book_obj = Booking.objects.get(booking_id=booking_id)
        box_obj = BoxBarcode.objects.filter(booking_id=booking_id)
        print(box_obj)
        return render(request, 'pod_details.html', {'data2': box_obj, 'data1': book_obj, 'data': user_obj})
    else:
        return redirect('/')
