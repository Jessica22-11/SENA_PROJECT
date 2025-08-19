from django.urls import path
from . import views
from .views import SolicitudAdmisionFormView

app_name = 'admisiones'

urlpatterns = [
    path('inscripcion/', views.SolicitudAdminsionForm, name='inscripcion_aspirante'),
    path('panel_coordinador/', views.panel_coordinador, name='panel_coordinador'),
    path('detalle_solicitud/<int:pk>/', views.detalle_solicitud, name='detalle_solicitud'),
    path('estado_aspirante/', views.estado_aspirante, name='estado_aspirante'),
    path('crear_solicitud/', SolicitudAdmisionFormView.as_view(), name='crear_solicitud'),
]

