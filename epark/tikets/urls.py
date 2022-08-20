from django.urls import path 
from . import views

app_name = 'tikets'
urlpatterns = [
    path('', views.tiket, name='tiket'),
    
]