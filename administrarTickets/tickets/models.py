# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Ticket(models.Model):
    fechaEmision=models.DateField()
    ciudadesO=('Esmeraldas','Esmeraldas'),('Manabi','Manabi'),('Quito','Quito'),('Guayaquil','Guayaquil'),('Latacunga','Latacunga')
    ciudadO=models.CharField(max_length=10, choices=ciudadesO,default='Guayaquil')
    ciudadesD=('Esmeraldas','Esmeraldas'),('Manabi','Manabi'),('Quito','Quito'),('Guayaquil','Guayaquil'),('Latacunga','Latacunga')
    ciudadD=models.CharField(max_length=10, choices=ciudadesD,default='Guayaquil')
    precio=models.FloatField()
    cedula=models.CharField(max_length=10)
    puesto=models.CharField(max_length=3)
