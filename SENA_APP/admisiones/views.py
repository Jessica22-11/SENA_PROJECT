from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import SolicitudAdmision
from .forms import SolicitudAdmisionForm

from django.views import generic
from django.contrib import messages
from django.views.generic import FormView
# Create your views here.

#Formulario de inscripción
def inscripcion_aspirante(request):
    if request.method == 'POST':
        form = SolicitudAdmisionForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Solicitud de admisión enviada correctamente.")
                return redirect ('admisiones:estado_aspirante')
            except Exception as e:
                messages.error(request, f"Error al enviar la solicitud: {str(e)}")
    else: 
        form = SolicitudAdmisionForm()
        return render(request,'admisiones/frormulario_isncripcion.html',{'form': form})
    
#Panel de revison de coordinador
def panel_coordinador(request):
    solicitudes = solicitudAdmision.objects.all().order_by('-fecha_solicitud')
    