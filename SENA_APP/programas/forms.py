from django import forms
from .models import Programa

class ProgramaForm(forms.Form):
    codigo = forms.CharField(max_length=20, label="Código del programa", help_text="Ingrese el código único del programa.")
    nombre = forms.CharField(max_length=200, label="Nombre del programa", help_text="Ingrese el nombre completo del programa.")
    nivel_formacion = forms.ChoiceField(choices=Programa.NIVEL_FORMACION_CHOICES, label="Nivel de Formación", help_text="Seleccione el nivel de formación del programa.")
    modalidad = forms.ChoiceField(choices=Programa.MODALIDAD_CHOICES, initial='PRE', label="Modalidad", help_text="Seleccione la modalidad del programa.")
    duracion_meses = forms.IntegerField(label="Duración en Meses", help_text="Ingrese la duración del programa en meses.")
    duracion_horas = forms.IntegerField(label="Duración en Horas", help_text="Ingrese la duración del programa en horas.")
    descripcion = forms.CharField(label="Descripción del Programa", widget=forms.Textarea, help_text="Ingrese una descripción detallada del programa.")
    competencias = forms.CharField(label="Competencias a Desarrollar", widget=forms.Textarea, help_text="Ingrese las competencias que se desarrollarán en el programa.")
    perfil_egresado = forms.CharField(label="Perfil de Egreso", widget=forms.Textarea, help_text="Ingrese el perfil del egresado del programa.")
    requisitos_ingreso = forms.CharField(label="Requisitos de Ingreso", help_text="Ingrese los requisitos necesarios para ingresar al programa.")
    centro_formacion = forms.CharField(max_length=200, label="Centro de Formación", help_text="Ingrese el nombre del centro de formación donde se ofrece el programa.")
    regional = forms.CharField(max_length=100, label="Regional", help_text="Ingrese la regional a la que pertenece el programa.")
    estado = forms.ChoiceField(choices=Programa.ESTADO_CHOICES, initial='ACT', label="Estado", help_text="Seleccione el estado actual del programa.")
    fecha_creacion = forms.DateField(label="Fecha de Creación del Programa", help_text="Ingrese la fecha de creación del programa.")    
    fecha_registro = forms.DateTimeField(widget=forms.HiddenInput(), required=False, label="Fecha de Registro", help_text="Fecha de registro del programa, se asigna automáticamente.")
    
    def clean(self):
        cleaned_data = super().clean()
        codigo = cleaned_data.get('codigo')
        nombre = cleaned_data.get('nombre')

        if not codigo or not nombre:
            raise forms.ValidationError("Todos los campos son obligatorios.")

        return cleaned_data
    
    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        if not codigo.isdigit():
            raise forms.ValidationError("El código debe contener solo números.")
        return codigo
    
    def save(self):
        try:
            programa = Programa.objects.create(
                codigo=self.cleaned_data['codigo'],
                nombre=self.cleaned_data['nombre'],
                nivel_formacion=self.cleaned_data['nivel_formacion'],
                modalidad=self.cleaned_data['modalidad'],
                duracion_meses=self.cleaned_data['duracion_meses'],
                duracion_horas=self.cleaned_data['duracion_horas'],
                descripcion=self.cleaned_data['descripcion'],
                competencias=self.cleaned_data['competencias'],
                perfil_egresado=self.cleaned_data['perfil_egresado'],
                requisitos_ingreso=self.cleaned_data['requisitos_ingreso'],
                centro_formacion=self.cleaned_data['centro_formacion'],
                regional=self.cleaned_data['regional'],
                estado=self.cleaned_data['estado'],
                fecha_creacion=self.cleaned_data['fecha_creacion'],
                fecha_registro=self.cleaned_data.get('fecha_registro', None)
            )
            return programa
        except Exception as e:
            raise forms.ValidationError(f"Error al guardar el programa: {str(e)}")