from django import forms
from .models import Productos

class formulario(forms.ModelForm):

    class Meta:
        model = Productos
        fields = ['nombre', 'precio', 'cantidad']