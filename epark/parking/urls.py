from django.urls import path
from . import views

urlpatterns = [
    path('search', views.ParkingSearchListView.as_view(), name='search'),
    path('<slug:slug>', views.ParkingDetailView.as_view(), name='parking'),

]