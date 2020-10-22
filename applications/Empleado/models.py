from django.db import models
from  applications.Departamento.models import Departamento

#ckeditor
from ckeditor.fields import RichTextField


# Create your models here.
class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name='Habilidad'
        verbose_name_plural='Habilidades de empleado'
        ordering=['habilidad'] #Orden inverso [-'name'], soporta muchos atributos ya que es una lista
        #unique_together=('first_name','last_name')
    def __str__(self):
        return "{}".format(self.habilidad)

class Empleado(models.Model):
    JOB_CHOICES= (
        ('0', 'Titular'),
        ('1', 'Rotar en plantilla'),
        ('2', 'Esporadico'),
        ('3', 'Otro'),
    )
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellido', max_length=60)
    full_nam = models.CharField(
            'Nombre completo', 
            max_length=120,
            blank=True)
    job = models.CharField('Trabajo', max_length=1,choices=JOB_CHOICES)
    #uno a muchos
    departamento_id = models.ForeignKey( Departamento, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='empleado', blank=True, null=True)
    
    #muchos a muchos
    habilidades = models.ManyToManyField(Habilidades)

    #ckeditor
    hoja_vida = RichTextField()

    class Meta:
        verbose_name='Empleado'
        verbose_name_plural='Empleados'
        ordering=['id'] #Orden inverso [-'name'], soporta muchos atributos ya que es una lista
        unique_together=('first_name','last_name')#impide una combinacion de valores
    
    def __str__(self):
        return "{} - {}".format(self.first_name, self.last_name)



