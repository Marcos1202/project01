
from django.contrib import admin
from django.urls import path
from . import views

app_name='departamento_app'
urlpatterns = [
   path(
      'nuevo-departamento/', 
      views.NuevoDepartementoView.as_view(), 
      name='nuevo_depto'),
      path(
      'departamentos/', 
      views.DepartamentoListView.as_view(), 
      name='departamentos'),
      

]
