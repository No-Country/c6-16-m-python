from .models import Tiket

def get_or_create_tiket(request):
    # Crear sesion
    # obtenemos el usuario authenticado
    user = request.user if request.user.is_authenticated else None
    tiket_id = request.session.get('tiket_id') # Si existe nos retorna el tiket sino retorna None
    tiket = Tiket.objects.filter(tiket_id=tiket_id).first() # Retorna elemento sino None
    
    # si el tiket no existe
    if tiket is None:
        # se crea un tiket
        tiket = Tiket.objects.create(user=user)

    if user and tiket.user is None: #Si el usuario existe y el tiket no posee usuario
        # Se asigna el tiket al usuario logeado.
        tiket.user = user 
        tiket.save()

    request.session['tiket_id'] = tiket.tiket_id

    return tiket