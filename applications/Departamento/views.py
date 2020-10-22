from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .forms import NuevoDepartamentoForm

from applications.Empleado.models import Empleado
from .models import Departamento
#la vista generica que utilizamos para formularios
#que no estan vinculados a un solo modelo se llama
#FormView
class NuevoDepartementoView(FormView):
    """NuevoDepartementoView definition."""
    template_name = 'departamento/nuevo_departamento.html'
    form_class = NuevoDepartamentoForm
    success_url = '.'

    #esta funcion es obligatoria
    def form_valid (self, form):

        dep = Departamento(
            name= form.cleaned_data['departamento'],
            shor_name= form.cleaned_data['shortname'],

        )
        dep.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job='1',
            departamento_id=dep
        )
        return super(NuevoDepartementoView, self).form_valid(form)

class DepartamentoListView(ListView):
    model = Departamento
    template_name = "Departamento/todos_departamentos.html"
    paginate_by = 5
