from django import forms
from .models import Categoria,Marca

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre',)

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ('nombre',)
