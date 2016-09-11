from django.shortcuts import get_object_or_404
from django.views.generic import *
from .models import *
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from DeseosAduaneros.forms import DeseoForm


class IndexView(ListView):
    template_name = 'DeseosAduaneros/index.html'
    context_object_name = 'lista_personajes'
    queryset = Personaje.objects.all()
    #serializer_class = DeporteSerializer

    def get_queryset(self):
        return Personaje.objects.all()


class DeseosViewList(ListView):
    template_name = 'DeseosAduaneros/deseos.html'
    context_object_name = 'lista_deseos'
    personaje = Personaje

    def get_queryset(self):
        self.personaje = get_object_or_404(Personaje, id=int(self.kwargs['personaje_id']))
        return Deseo.objects.filter(personaje__pk=self.personaje.pk)

    def get_context_data(self, **kwargs):
        context = super(DeseosViewList, self).get_context_data(**kwargs)
        context['personaje'] = self.personaje
        return context


class DeseosView(CreateView):
    model = Deseo
    template_name = "DeseosAduaneros/registrarDeseo.html"
    form_class = DeseoForm
    success_url = reverse_lazy('DeseosAduaneros:index')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(DeseosView, self).form_valid(form)


class DeseosEditView(UpdateView):
    model = Deseo
    template_name = "DeseosAduaneros/actualizarDeseo.html"
    form_class = DeseoForm
    success_url = reverse_lazy('DeseosAduaneros:index')


class DeseosDeleteView(DeleteView):
    model = Deseo
    template_name = "DeseosAduaneros/eliminarDeseo.html"
    success_url = reverse_lazy('DeseosAduaneros:index')