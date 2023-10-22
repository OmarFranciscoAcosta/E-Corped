import email
from email.message import EmailMessage
from msilib.schema import Class
from django.db import models
from aplications.departamento.models import Departamento
from tkinter import *
# Create your models here.
class EstCiv (models.Model):
    estadocivil = models.CharField('Estado Civil', max_length=50, blank=True)
    
    class Meta:
        verbose_name = 'Estado Civil'
        verbose_name_plural = 'Estados Civiles'
        ordering = ['estadocivil']
        unique_together = ('estadocivil',)
    def __str__(self):
        return self.estadocivil

class Habilidades (models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)
    
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades del empleado'
        ordering = ['habilidad']
        unique_together = ('habilidad',)
    def __str__(self):
        return self.habilidad
class Empleado (models.Model):
    # Modelo para la tabla empleados general
    
    JOB_CHOICES =(
        ('0','Contador'),
        ('1','Administrativo'),
        ('2','Desarrollador'),
        ('3','Analista Funcional'),
        ('4','Otro'),
    )
    
    nombre = models.CharField('Nombre', max_length=60)
    apellido = models.CharField('Apellido', max_length=50)
    trabajo = models.CharField('Trabajo', max_length=1, choices = JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    Situacion = models.ManyToManyField(EstCiv)
    Habilidad = models.ManyToManyField(Habilidades)
    email = models.EmailField('Mail',blank = True)
    imagen_de_perfil = models.ImageField('Foto de perfil', upload_to='static/images',blank=True, null=True)
    class Meta:
        verbose_name = 'Mi empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['-nombre','apellido']
        unique_together = ('nombre','departamento','email')
    def __str__(self):
        return self.nombre + '-' + self.apellido
        