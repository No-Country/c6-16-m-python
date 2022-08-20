from django.shortcuts import render
from .models import Tiket

# Create your views here.
def tiket(request):    
    # Crear sesion
    # obtenemos el usuario authenticado
    user = request.user if request.user.is_authenticated else None
    tiket_id = request.session.get('tiket_id')
    
    if tiket_id:
        # obtenemos el tiket de la base de datos si existe
        tiket = Tiket.objects.get(tiket_id=tiket_id)
        # creamos un tiket
    else:
        tiket = Tiket.objects.create(user=user)    

    request.session['tiket_id'] = tiket.tiket_id
    return render(request, 'tikets/tiket.html', {})