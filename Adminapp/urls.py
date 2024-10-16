from django.urls import path
from Adminapp import views
urlpatterns = [
    path('add_designation',views.add_designation),
    path('add_user',views.add_user),
    path('list_user',views.list_user),
    path('delete_user/<int:user_id>/',views.delete_user),
    path('edit_user/<int:user_id>/',views.edit_user),
    path('',views.login),
    path('dashboard',views.dashboard),
    path('signout',views.signout),
    #path('staff_dashboard',views.staff_dashboard),
    path('add_consignor', views.add_consignor),
    path('list_consignor',views.list_consignor),
    path('delete_consignor/<int:consignor_id>/',views.delete_consignor),
    path('edit_consignor/<int:consignor_id>/',views.edit_consignor),
    path('list_designation',views.list_designation),
    path('delete_designation/<int:designation_id>/',views.delete_designation),
    path('edit_designation/<int:designation_id>/',views.edit_designation),
    path('add_consignee',views.add_consignee),
    path('list_consignee',views.list_consignee),
    path('delete_consignee/<int:consignee_id>/',views.delete_consignee),
    path('edit_consignee/<int:consignee_id>/',views.edit_consignee),
    path('add_district',views.add_district),
    path('list_district',views.list_districts),
    path('delete_district/<int:district_id>/',views.delete_district),
    path('edit_district/<int:district_id>/',views.edit_district),
    path('add_driver',views.add_driver),
    path('list_driver',views.list_drivers),
    path('delete_driver/<int:driver_id>/',views.delete_driver),
    path('edit_driver/<int:driver_id>/',views.edit_driver),
    path('add_vehicle',views.add_vehicle),
    path('list_vehicle',views.list_vehicle),
    path('delete_vehicle/<int:vehicle_id>/',views.delete_vehicle),
    path('edit_vehicle/<int:vehicle_id>/',views.edit_vehicle),
    path('list_booking',views.list_booking),
    path('delete_booking/<int:booking_id>/',views.delete_booking),
]