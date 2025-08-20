from django.db import models

# Create your models here.    
class SolicitudAdmision(models.Model):
    TIPO_DOCUMENTO_ESTADO_CHOICES = [
        ('TI', 'Tarjeta de identidad'),
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería'),
        ('PP', 'Pasaporte'),
        ('RC',  'Registtro Civil'),
    ]
    
    ESTADO_CHOICES = [
        ('REV', 'En Revisión'),
        ('ADM', 'Admitido'),
        ('REC', 'Rechazado'),
    ]
    nombre_completo = models.CharField(max_length=100, unique=True)
    tipo_documento = models.CharField(max_length=10, choices=TIPO_DOCUMENTO_ESTADO_CHOICES, default='CC')
    numero_documento = models.CharField(max_length=10, unique=True)
    correo = models.EmailField(null=True)
    telefono = models.IntegerField(max_length=10, unique=True)
    programa = models.ForeignKey('programas.Programa', on_delete=models.CASCADE, verbose_name="Programa de Formación")
    documento_identidad = models.FileField(upload_to='admisiones/documento_identidad/', null=True, blank=True)
    certificado_academico = models.FileField(upload_to='admisiones/cartificado_academmico/', null=True, blank=True)
    certificado_eps = models.FileField(upload_to='admisiones/certificado_eps/', null=True, blank=True)
    estado = models.CharField(max_length=3, choices=ESTADO_CHOICES, default='ADM', verbose_name="Estado de la Solicitud")
    fecha_solicitud = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Solicitud")
    
    def __str__(self):
        return f"{self.nombre_completo} - {self.estado}"