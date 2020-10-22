from django.shortcuts import render
#paqute para enviar a una url
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView, 
    DeleteView
)
from .forms import EmpleadoForm

#clase para el home
class InicioHome(TemplateView):
    template_name = "index.html"


#list view  requiere un qery set o medelo para trabajar
from .models import Empleado

#vista todos los empleadors

class EmpleadosListView(ListView):
   
    #paginacion
    template_name = "Empleado/list_all.html"
    paginate_by = 4
    ordering = 'first_name' 

    def get_queryset(self):
        #interceptar datos enviados por formulario
        palabra_clave = self.request.GET.get("kword", "")
        #__icontains busca palabras que coincidan
        lista =  Empleado.objects.filter(
            full_nam__icontains =  palabra_clave
        )
       
        return lista


class EmpleadosEditarListView(ListView):
   
    #paginacion
    template_name = "Empleado/lista_editar.html"
    paginate_by = 10
    ordering = 'first_name'
    context_object_name  =  'empleados'
    model = Empleado


class ListByAreaListView(ListView):
    """  queryset = Empleado.objects.filter(
        departamento_id__name='Area contable'
        ) """
    template_name = "Empleado/list_area.html"
    paginate_by = 4
    
     
        #sobreescribimos una funcion de las vistas en listviewtree 
    def get_queryset(self):
        #recogemos un parametro del url
        area = self.kwargs['shorname']
        
        lista =  Empleado.objects.filter(
        departamento_id__shor_name=area
        )
        #para esta funcion siempre debemos retornar una lista
        return lista



class ListByJobListView(ListView):
    template_name = "Empleado/list_job.html"
    #context_object_name = "empleados"
        #sobreescribimos una funcion de las vistas en listviewtree 
    def get_queryset(self):
        #recogemos un parametro del url
        job = self.kwargs['shorname']        
        lista =  Empleado.objects.filter(
        job=job
        )
        print(lista)
        #para esta funcion siempre debemos retornar una lista
        return lista


class ListEmpleadosWKListView(ListView):
    model = Empleado
    template_name = "empleado/by_kword.html"
    #variable para trabajarla en el html (no necesaria)
    context_object_name='empleados'
    def get_queryset(self):
        #interceptar datos enviados por formulario
        palabra_clave = self.request.GET.get("kword", "")
        lista =  Empleado.objects.filter(
        first_name=palabra_clave
        )
        return lista


class HabilidadesListView(ListView):
    template_name = "Empleado/habilidades.html"
    context_object_name = 'habilidades'
    #model = Habilidades

    def get_queryset(self):
        emp = self.kwargs['id']
        
        #metodo get recupera un unico  registro
        empleado = Empleado.objects.get(id=emp)       
        return empleado.habilidades.all()
 
#Esta clase nos ayuda para mostrar mas detalles

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "Empleado/detalle_empleado.html"

    """Sobre escribiendo un metodo para enviar una variable
    al front """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Empleado del mes'
        return context

#vista basica
""" Usaremos esta clase (vista basica) con el unico proposito 
de que despues de guardar un emleado nos mande a este template """
class SuccessView(TemplateView):
    template_name = "Empleado/success.html"


# Vista generica para Registrar algo en el modelo de la base de datos 
class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "Empleado/add.html"
    #Aqui llamamos a todos los campos del modelo
    #fields = ('__all__')
    """ Sin no queremos agregar todos los campos del modelo usamos:"""
    #fields = ['first_name', 'last_name', 'job', 'departamento_id', 'habilidades','image'] 
    #Aqui indicamos a donde quremos que nos lleve la pagina al completar el formulario
    #en este ejemplo solo recargaremos la pagina
    #success_url = '.'
    #Asi indicamos el envio a otra pagina
    #success_url = '/success'
    #asi usando el paquete de la segunda linea de este archivo
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleado_app:todos-empleados')

    #funcion para crear el full name
    def form_valid(self, form):
        #commit = False ayuda a no generar un doble guardado
        empleado = form.save(commit = False)
        empleado.full_nam = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "Empleado/update.html"

    form_class = EmpleadoForm
    """ fields = [
        'first_name', 
        'last_name', 
        'job', 
        'departamento_id', 
        'habilidades'
    ] """
    success_url = reverse_lazy('empleado_app:editar_empleados')

    #este metodo podemos usarlo en el create view tambien
    # proceso para guardar datos antes de ser validados
    #def post(self, request, *args, **kwargs):
    #    print(request.POST)
    #    return super().post(request, *args, **kwargs) 


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "Empleado/delete.html"
    success_url = reverse_lazy('empleado_app:editar_empleados')


