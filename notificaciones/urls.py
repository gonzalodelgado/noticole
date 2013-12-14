from __future__ import unicode_literals

from django.conf.urls import patterns, url

from notificaciones.views import NotificacionesView


urlpatterns = patterns("",
    url(r"^$", NotificacionesView.as_view(), name="home"),
)
