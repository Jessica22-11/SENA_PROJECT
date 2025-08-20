from django.urls import path
from . import views
from .views import SolicitudAdmisionFormView

app_name = 'admisiones'

urlpatterns = [
    path('admisiones/', SolicitudAdmisionFormView.as_view(), name='formulario_inscripcion'),
    path('panel_coordinador/', views.panel_coordinador, name='panel_coordinador'),
    path('detalle_solicitud/<int:pk>/', views.detalle_solicitud, name='detalle_solicitud'),
    path('estado_aspirante/', views.estado_aspirante, name='estado_aspirante'),
    path('rechazar/<int:pk>/', views.rechazar_solicitud, name='rechazar_solicitud'),
    path('aprobar/<int:pk>/', views.aprobar_solicitud, name='aprobar_solicitud'),
]

