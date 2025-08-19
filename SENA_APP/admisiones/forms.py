from django import forms
from .models import SolicitudAdmision

class SolicitudAdminsionForm9(forms.Form):
    nombre_completo = forms.CharField(max_length=100, label='Nombre Completo', help_text='Ingrese su nombre compelto.')