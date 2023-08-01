from django.contrib import admin
from .models import Reservation
from escaperoom.models import Room_Description

admin.site.register(Reservation)
admin.site.register(Room_Description)
