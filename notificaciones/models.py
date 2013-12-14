from django.db import models
from django.contrib.auth.models import Group


class Alumno(models.Model):
    usuario = models.OneToOneField(
        'auth.User', limit_choices_to={'groups': Group.objects.get(name='Alumnos')},
        null=True, blank=True)
    padre = models.ForeignKey('auth.User', related_name='hijos', limit_choices_to={'groups': Group.objects.get(name='Padres')})
    foto = models.ImageField(upload_to='alumnos', null=True)

    def nombre(self):
        return self.usuario.get_full_name()

    def __unicode__(self):
        return self.nombre()


TIPOS = (
    ('falta', 'Falta'),
    ('disciplinario', 'Medida disciplinaria'),
    ('fecha', 'Fecha Importante'),
    ('examen', 'Fecha de Examen'),
    ('nota', 'Nota de examen'),
    ('observacion', 'Observaciones'),
)

class Notificacion(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=100, choices=TIPOS)
    mensaje = models.TextField(blank=True)
    permitir_comentarios = models.BooleanField()
    notificador = models.ForeignKey('auth.User', editable=False)
    alumno = models.ForeignKey(Alumno, null=True, blank=True)
    grupo = models.ForeignKey('auth.Group', null=True, blank=True)

    class Meta:
        ordering = '-timestamp',
        verbose_name_plural = 'Notificaciones'

    def nivel(self):
        niveles = {'fecha': 'info', 'examen': 'info',
                   'nota': 'success', 'observacion': 'info',
                   'falta': 'warning', 'disciplinario': 'danger'}
        return niveles.get(self.tipo)
