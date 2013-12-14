from django.contrib import admin

from notificaciones.models import Alumno, Notificacion


class NotificacionAdmin(admin.ModelAdmin):
    list_display = 'tipo', 'alumno', 'mensaje'

    def save_model(self, request, obj, form, change):
        obj.notificador = request.user
        super(NotificacionAdmin, self).save_model(request, obj, form, change)


class AlumnoAdmin(admin.ModelAdmin):
    list_display = 'nombre', 'padre'



admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Notificacion, NotificacionAdmin)
