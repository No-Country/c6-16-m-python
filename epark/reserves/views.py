
from django.shortcuts import render
from .models import Reserve
from .utils import get_or_create_reserve
from parking.models import Parking
# Create your views here.
def reserve(request):    
    reserve = get_or_create_reserve(request)    
    
    return render(request, 'reserves/reserve.html', {})

def add(request):
    reserve = get_or_create_reserve(request)
    # obtiene el producto del formulario, con su name parking_id declarado en add.html
    parking = Parking.objects.get(pk=request.POST.get('parking_id'))    
    # Se agrega el objeto de reserva a la relacion reserve-parking
    reserve.parkings.add(parking)    #reserve.parkings.add(parking)
   
    return render(request, 'reserves/add.html', {
        'parking': parking
    })