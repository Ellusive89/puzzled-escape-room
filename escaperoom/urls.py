from django.urls import path

from . import views

urlpatterns = [
    path('', views.escaperoom_page_view, name='escaperoom'),
]
