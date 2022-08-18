from cProfile import label
from django import forms

from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    name = forms.CharField(label='Nombre',required=True,max_length=255, widget=forms.TextInput(attrs={'class': "form-input", 'placeholder':'Nombre'}))    
    lastname = forms.CharField(label='Apellido', required=True,max_length=255, widget=forms.TextInput(attrs={'class': "form-input", 'placeholder':'Apellido'}))
    email = forms.EmailField(label='Escriba su E-mail', required=True,widget=forms.TextInput(attrs={'class': "form-input", 'placeholder':'E-mail'}))    
    phone = forms.CharField(label='telefono',required=True,widget=forms.TextInput(attrs={'class': "form-input", 'placeholder':'Numero de Telefono'}))
    country = forms.CharField(label='Pais',required=True,max_length=255, widget=forms.TextInput(attrs={'class': "form-input", 'placeholder':'Su nacionalidad'}))
    city = forms.CharField(label='Ciudad',required=True,max_length=255, widget=forms.TextInput(attrs={'class': "form-input", 'placeholder':'Su Ciudad'}))
    password = forms.CharField(label='Contraseña',required=True, widget=forms.PasswordInput(attrs={'class': "form-input", 'placeholder':'Escriba su contraseña'}))
    password2 = forms.CharField(label='Repetir contraseña', required=True, widget=forms.PasswordInput(attrs={'class': "form-input", 'placeholder':'Repita su contraseña'}))
    
    def clean_email(self):
        # obtiene la informacion del input 
        email = self.cleaned_data.get('email')
        # exister el name o no 
        if User.objects.filter(email=email).exists():
             # si existe un usuario con ese name
            raise forms.ValidationError('El email ya existe')
        return email

    def clean(self):
        # obtiene todos los campos dle formulario
        cleaned_data = super().clean()

        # si las contraseñas son diferentes
        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'Las contraseñas no coinciden')

    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('name'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),
        )



