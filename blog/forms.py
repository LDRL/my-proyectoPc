from django import forms
from .models import Categoria,Marca
from .models import Computadora
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre',)

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ('nombre',)

class CompuForm(forms.ModelForm):
    class Meta:
        model = Computadora
        fields=('autor','precio','descripcion','categoria','marca','imagen',)
