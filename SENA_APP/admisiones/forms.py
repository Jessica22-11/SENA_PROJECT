from django import forms
from .models import SolicitudAdmision


class SolicitudAdminsionForm(forms.Form):
    nombre_completo = forms.CharField(max_length=100, label='Nombre Completo', help_text='Ingrese su nombre compelto.')
    tipo_documento = forms.ChoiceField(choices=SolicitudAdmision.TIPO_DOCUMENTO_ESTADO_CHOICES, label='Tipo de Documento', help_text='Seleccione el tipo de documento.')
    numero_documento = forms.CharField(max_length=10, label='Número de Docuemtno', help_text='Ingrese el número de documento.')
    correo = forms.EmailField(label='Correo Electrónico', help_text='Ingrese su correo electrónico.')
    telefono = forms.IntegerField(label='Teléfono', help_text='Ingrese su teléfono.')
    programa = forms.ModelChoiceField(queryset=SolicitudAdmision.objects.all(), label='Programa de Formación', help_text='Seleccione el programa de formación.')