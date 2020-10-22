from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    shor_name = models.CharField('Nombre corto', max_length=50)
    active = models.BooleanField('Activo',default=True)

    """
    para mandar una imagen en blanco necesitamos:
    null=true
    para dejar un campo opcional
    blanck =true
    Para crear un campo unico
    unique=true
    para que nadie pueda acceder desde el administradoor
    editable=false
    """

    class Meta:
        verbose_name='Mi departamento'
        verbose_name_plural='Areas de la empresa'
        ordering=['name'] #Orden inverso [-'name'], soporta muchos atributos ya que es una lista
        unique_together=('name','shor_name')#impide una combinacion de valores

    def __str__(self):
        return "{} - {}".format(self.name, self.active)