from django import forms
from .models import SolicitudAdmision
from programas.models import Programa


class SolicitudAdminsionForm(forms.Form):
    nombre_completo = forms.CharField(max_length=100, label='Nombre Completo', help_text='Ingrese su nombre compelto.')
    tipo_documento = forms.ChoiceField(choices=SolicitudAdmision.TIPO_DOCUMENTO_ESTADO_CHOICES, label='Tipo de Documento', help_text='Seleccione el tipo de documento.')
    numero_documento = forms.CharField(max_length=10, label='Número de Docuemtno', help_text='Ingrese el número de documento.')
    correo = forms.EmailField(label='Correo Electrónico', help_text='Ingrese su correo electrónico.')
    telefono = forms.IntegerField(label='Teléfono', help_text='Ingrese su teléfono.')
    programa = forms.ModelChoiceField(queryset=Programa.objects.all(), label='Programa de Formación', help_text='Seleccione el programa de formación.')
    documento_identidad = forms.FileField(label='Documento de Identidad', help_text='Suba su documento de identidad.')
    certificado_academico = forms.FileField(label='Certificado Académico', help_text='Suba su certificado académico.')
    certificado_eps = forms.FileField(label='Certificado eps', help_text='Suba su certificado de eps')
    estado = forms.ChoiceField(choices=SolicitudAdmision.ESTADO_CHOICES, initial='REV', label='Estado de la Solicitud', help_text='Estado actual de la solicitud se asigna por el sistema.')
    fecha_solicitud = forms.DateTimeField(label='Fecha de Solicitud', help_text='Fecha de la solicitud.')
    
    def clean(self):
        cleaned_data = super().clean()
        numero_documento = cleaned_data.get('documento_identidad')
        nombre_completo = cleaned_data.get('nombre_completo')
        
        if not numero_documento or not nombre_completo:
            raise forms.ValidationError('Todos los campos son obligatorios.')
        
        return cleaned_data
    
    def clean_numero_documento(self):
        numero_documento = self.cleaned_data.get['numero_documento']
        if not numero_documento.isdigit():
            raise forms.ValidationError('El documento debe tener solo números.')
        return numero_documento
    
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono and not telefono.isdigit():
            raise forms.ValidationError("El teléfono debe tener solo números.")
        return telefono
    
    def save(self):
        try:
            solicitud = SolicitudAdmision.objects.create(
                nombre_completo=self.cleaned_data['nombre_completo'],
                tipo_documento=self.cleaned_data['tipo_documento'],
                numero_documento=self.cleaned_data['numero_documento'],
                correo=self.cleaned_data['correo'],
                telefono=self.cleaned_data['telefono'],
                programa=self.cleaned_data['programa'],
                documento_identidad=self.cleaned_data['documento_identidad'],
                certificado_academico=self.cleaned_data['certificado_academico'],
                certificado_eps=self.cleaned_data['certificado_eps'],
                estado=self.cleaned_data.get('estado', 'REV'),
                fecha_solicitud=self.cleaned_data.get('fecha_solicitud', None)
            )
            return solicitud
        except Exception as e:
            raise forms.ValidationError(f"Error al guardar la solicitud: {str(e)}")
        