from django.http import HttpResponse
from .models import Aprendiz
from django.template import loader

def aprendices(request):
    lista_aprendices = Aprendiz.objects.all().order_by('nombre', 'apellido')
    template = loader.get_template('lista_aprendices.html')
    context = {
        'lista-aprendices' :lista_aprendices,
        'total_aprendices': lista_aprendices.count(),
    }
    return HttpResponse(template.render(context, request))

def  inicio(request):
    template = loader.get_template('inicio.html')
    return HttpResponse(template.render())