
from django.shortcuts import render
from .models import Tiket
from .utils import get_or_create_tiket
from parking.models import Parking
# Create your views here.
def tiket(request):    
    tiket = get_or_create_tiket(request)    
    
    return render(request, 'tikets/tiket.html', {})

def add(request):
    tiket = get_or_create_tiket(request)
    # obtiene el producto del formulario, con su name parking_id declarado en add.html
    parking = Parking.objects.get(pk=request.POST.get('parking_id'))    
    # Se agrega el objeto de reserva a la relacion tiket-parking
    tiket.parkings.add(parking)    #tiket.parkings.add(parking)
   
    return render(request, 'tikets/add.html', {
        'parking': parking
    })