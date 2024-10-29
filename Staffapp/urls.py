from django.urls import path
from Staffapp import views

app_name = 'staff'
urlpatterns = [
    path('add_booking',views.add_booking, name='add_booking'),
    path('edit_booking/<int:booking_id>',views.edit_booking,name='edit_booking'),
    path('add_despatch',views.add_despatch, name='add_despatch'),
    path('add_delivery',views.add_delivery, name='add_delivery'),
]