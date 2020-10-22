
from django.contrib import admin
from django.urls import path

from . import views
""" Usamos la siguiente linea para darle un nombre a todo el congunto de urls 
    app_name"""

app_name = "empleado_app"

urlpatterns = [
    path('', views.InicioHome.as_view(), name='inicio'),
    path(
        'listar-empleados/', 
        views.EmpleadosListView.as_view(),
        name='todos-empleados'
    ),
    path(
        'listar-empleados-area/<shorname>/', 
        views.ListByAreaListView.as_view(),
        name='empleados_area'
        ),
    path(
        'listar-empleados-job/<shorname>/', 
        views.ListByJobListView.as_view(),
        name='empleados_job'
    ),
    path(
        'buscar_empleado/', 
        views.ListEmpleadosWKListView.as_view()
    ),
    path(
        'listar-habilidades-empleado/<id>/', 
        views.HabilidadesListView.as_view()
    ),
    path(
        'detalle_empleado/<pk>/', 
        views.EmpleadoDetailView.as_view(),
        name='detalle_emp'
    ),
    path(
        'add_empleado/', 
        views.EmpleadoCreateView.as_view(),
        name='agregar_empleado'),
    # name = correcto es una etiqueta para llamar a esta url """
    path('success/', views.SuccessView.as_view(), name='correcto'),
    path(
        'update-empleado/<pk>/', 
        views.EmpleadoUpdateView.as_view(), 
        name='modificar_empleado'
    ),
    path(
         'delete-empleado/<pk>/', 
         views.EmpleadoDeleteView.as_view(), 
         name='eliminar_empleado'
        ),
    path(
         'admin-empleados/', 
         views.EmpleadosEditarListView.as_view(), 
         name='editar_empleados'
        ),
]
