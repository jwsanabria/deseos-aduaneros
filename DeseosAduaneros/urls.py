from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'DeseosAduaneros'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^deseos/(?P<personaje_id>[0-9]+)/$', views.DeseosViewList.as_view(), name='lista_deseos'),
    url(r'^registrarDeseo$', views.DeseosView.as_view(), name='registro_deseo'),
    url('^actualizarDeseo/(?P<pk>[\w-]+)$', views.DeseosEditView.as_view(), name='actualiza_deseo'),
    url('^eliminarDeseo/(?P<pk>[\w-]+)$', views.DeseosDeleteView.as_view(), name='elimina_deseo'),

]