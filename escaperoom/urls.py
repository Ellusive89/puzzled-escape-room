from django.urls import path

from . import views

urlpatterns = [
    path('', views.escaperoom_page_view, name='escaperoom'),
    path('booking', views.booking, name='booking'),
    path('booking-submit', views.bookingSubmit, name='bookingSubmit'),
    path('our-rooms', views.our_rooms, name='our_rooms'),
]
