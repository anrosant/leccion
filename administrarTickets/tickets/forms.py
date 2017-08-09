from django import forms

from django.db import models
from . models import Ticket
import datetime

class ticketForm(forms.ModelForm):
    class Meta:
        model=Ticket
        fechaEmision=models.DateField()
        ciudadesO=('Esmeraldas','Esmeraldas'),('Manabi','Manabi'),('Quito','Quito'),('Guayaquil','Guayaquil'),('Latacunga','Latacunga')
        ciudadO=models.CharField(max_length=10, choices=ciudadesO,default='Guayaquil')
        ciudadesD=('Esmeraldas','Esmeraldas'),('Manabi','Manabi'),('Quito','Quito'),('Guayaquil','Guayaquil'),('Latacunga','Latacunga')
        ciudadD=models.CharField(max_length=10, choices=ciudadesD,default='Guayaquil')
        precio=models.FloatField()
        cedula=models.CharField(max_length=10)
        puesto=models.CharField(max_length=3)
        fields=('fechaEmision','ciudadO','ciudadD','precio','cedula','puesto',)
