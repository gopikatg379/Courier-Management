from django.urls import path
from Staffapp import views
urlpatterns = [
    path('add_booking',views.add_booking),
    path('edit_booking/<int:booking_id>',views.edit_booking),
    path('add_despatch',views.add_despatch),
]