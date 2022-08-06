from django import forms

from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(required=True,max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'}))
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(label='repetir contraseña', required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}))

    # valida username
    def clean_username(self):
        # obtiene la informacion del input 
        username = self.cleaned_data.get('username')
        # exister el username o no 
        if User.objects.filter(username=username).exists():
             # si existe un usuario con ese username
            raise forms.ValidationError('El username ya existe')
        return username

    def clean_email(self):
        # obtiene la informacion del input 
        email = self.cleaned_data.get('email')
        # exister el username o no 
        if User.objects.filter(email=email).exists():
             # si existe un usuario con ese username
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
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),
        )



