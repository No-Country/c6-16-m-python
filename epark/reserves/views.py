
from django.shortcuts import render
from .models import Reserve
from .utils import get_or_create_reserve
from parking.models import Parking
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
# Create your views here.
def reserve(request):    
    reserve = get_or_create_reserve(request)    
    
    return render(request, 'reserves/reserve.html', {
        'reserve': reserve
    })

def add(request):
    reserve = get_or_create_reserve(request)
    # obtiene el producto del formulario, con su name parking_id declarado en add.html
    parking = Parking.objects.get(pk=request.POST.get('parking_id'))    
    # Se agrega el objeto de reserva a la relacion reserve-parking
    reserve.parkings.add(parking)    #reserve.parkings.add(parking)
   
    return render(request, 'reserves/add.html', {
        'parking': parking
    })

def remove(request):
    reserve = get_or_create_reserve(request)
    parking = get_object_or_404(Parking, pk=request.POST.get('parking_id'))    

    reserve.parkings.remove(parking)

    return redirect('reserves:reserve')