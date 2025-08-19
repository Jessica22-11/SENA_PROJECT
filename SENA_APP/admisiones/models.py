from django.db import models

# Create your models here.
class SolicitudAdmision(models.Model):
    nombre_completo = models.Charfiel(max_length=100, unique=True)
    tipo_documento = models.Charfield