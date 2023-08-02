from django.urls import path

from . import views

urlpatterns = [
    path('', views.escaperoom_page_view, name='escaperoom'),
    path('escaperoom.html', views.escaperoom_page_view, name='escaperoom'),
    path('booking', views.booking, name='booking'),
    path('booking-submit', views.bookingSubmit, name='bookingSubmit'),
    path('our-rooms', views.our_rooms, name='our_rooms'),
    path('user-panel', views.user_panel, name='user_panel'),
    path('user-update/<int:id>', views.user_update, name='user_update'),
    path('user-update-submit/<int:id>', views.user_updateSubmit, name='user_updateSubmit'),
    path('user-delete/<int:id>', views.user_delete, name='user_delete'),
]
