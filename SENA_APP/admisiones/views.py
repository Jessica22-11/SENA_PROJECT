from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import SolicitudAdmision
from django.urls import reverse_lazy
from admisiones.forms import SolicitudAdminsionForm


from django.views import generic
from django.contrib import messages
from django.views.generic import FormView
# Create your views here.

#Formulario con FormView para crear solicitud
class SolicitudAdmisionFormView(FormView):
    template_name = 'formulario_inscripcion.html'
    form_class = SolicitudAdminsionForm
    success_url = reverse_lazy('admisiones')  

    def form_valid(self, form):
        form.save()  # guarda la solicitud en la base de datos
        messages.success(self.request, "Tu solicitud fue enviada correctamente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Hubo un error en el formulario. Verifica los datos.")
        return super().form_invalid(form)


#Panel de revison de coordinador
def panel_coordinador(request):
    solicitudes = SolicitudAdmision.objects.all().order_by('-fecha_solicitud')
    return render (request, 'admisiones/panel_coordinador.html', {'solicitudes': solicitudes})

#Detalle de la solicitud
def detalle_solicitud(request,pk):
    solicitud = get_object_or_404(SolicitudAdmision, pk=pk)
    
    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado')
        if nuevo_estado and nuevo_estado in dict(SolicitudAdmision.ESTADO_CHOICES):
            solicitud.estado = nuevo_estado
            solicitud.save()
            messages.success(request, "Estado de la solicitud actualizado correctamente.")
            return redirect('admisiones:panel_coordinador')
        return render(request, 'admisiones/detalle_solicitud.html', {'solicitud': solicitud})
    
#Estado de inscripcion del aspirante
def estado_aspirante(request):
    numero_documento = request.GET.get('numero_documento', None)
    solicitu = None
    if numero_documento:
        try:
            solicitud = SolicitudAdmision.objects.get(numero_documento=numero_documento)
        except SolicitudAdmision.DoesNotExist:
            messages.error(request, "No se encontró ninguna solicitud con ese número de documento.")
    return render(request, 'admsiones/estado_aspirante.html', {'solicitud': solicitud})
