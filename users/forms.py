from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Producto ,Servicio

class Nuevo_ProdForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('modelo','estado')

class Nuevo_ServForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = (
            'hora_atencion',
            'descripcion_cliente',
            )
            
class Nuevo_EditServForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = (
            'tecnico',
            'hora_atencion',
            'cant_pers',
            'precio',
            'estado',
            'descripcion_cliente',
            'descripcion_tecnico',
            )

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','rut', 'email','tipo','fecha_nacimiento','sexo')

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'email','tipo','fecha_nacimiento','sexo')