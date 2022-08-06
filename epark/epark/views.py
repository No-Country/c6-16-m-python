from django.shortcuts import render 
from django.contrib import messages
from django.shortcuts import redirect

from django.contrib.auth import login
# genera la sesion
from django.contrib.auth import authenticate
# para autenticar usuarios

def index(request):
    return render(request, 'index.html')


def login_view(request):
    # request.method es POST cuando se toca el boton enviar en el login
    # si se presiono el boton, obtiene el input name username y password 

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # busca en la base de datos un usuario que tenga ese username y contranseña
        # si existe nos retorna un objeto User almacenable si no existe nos retorna NONE
        user = authenticate(username=username, password=password)
        
        if user: 
            # para generar una sesion necesita peticion (request) y el usuario (user)
            login(request, user)
            # Mensaje de login correcto 
            messages.success(request, "Bienvnido {}".format(username))
            # se debe colocar en el template si hay mensajes para visualizarlos
            
            # concretada lo anterior redirije al string que se coloca dentro. 
            return redirect('index')
        # Si user retorna NONE
        else:
            messages.error(request, "Usuario o Contraseña Incorrectos.")
            # se debe colocar en el template si hay mensajes para visualizarlos
            



    return render(request, 'users/login.html', {

    })

