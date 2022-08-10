from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>', views.ParkingDetailView.as_view(), name='parking'),

]