from django.db.models import Q
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from notificaciones.models import Notificacion


class NotificacionesView(ListView):
    template_name = 'notificaciones/list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NotificacionesView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        if self.request.user.is_superuser:
            notificaciones = Notificacion.objects.all()
        else:
            notificaciones = Notificacion.objects.filter(
                Q(alumno__padre=self.request.user)|Q(alumno__isnull=True, grupo__isnull=True))
        return notificaciones
