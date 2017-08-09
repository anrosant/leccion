from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Actualizar/(?P<tId>[0-9]+)$', views.actTicket, name='actTicket'),
    url(r'^actualizando/(?P<tId>[0-9]+)$', views.actualizar, name='actualizar'),
    url(r'^crear/$', views.crear, name='crear'),
    url(r'^eliminar/(?P<tId>[0-9]+)$', views.eliminar, name='eliminar'),
]
