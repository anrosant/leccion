# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import ticketForm
from .models import Ticket
from datetime import date

def index(request):
	template = loader.get_template('tickets/index.html')
	tickets = Ticket.objects.all()
	context = {
		'tickets': tickets,
	}
	return HttpResponse(template.render(context, request))

def actTicket(request, tId):
	ticket = Ticket.objects.get(id=tId)
	template = loader.get_template('tickets/actualizar.html')
	fechaEmision = ticket.fechaEmision
	fechaEmision = date(fechaEmision.year, fechaEmision.month, fechaEmision.day)
	context = {
		'tId': tId,
		'titulo': 'Actualización de Ticket',
		'action': 'Actualizar',
        'fechaEmision': fechaEmision.strftime("%Y-%m-%d"),
		'ciudadO': ticket.ciudadO,
        'ciudadD': ticket.ciudadD,
		'precio': ticket.precio,
		'cedula': ticket.cedula,
        'puesto': ticket.puesto,
	}
	return HttpResponse(template.render(context, request))

def crear(request):
	if request.method == "POST":
		form = ticketForm(request.POST)
		if form.is_valid():
			ticket = form.save(commit=False)
			ticket.fechaEmision=request.POST["fechaEmision"]
			ticket.ciudadO=request.POST["ciudadO"]
			ticket.ciudadD=request.POST["ciudadD"]
			ticket.precio=request.POST["precio"]
			ticket.cedula=request.POST["cedula"]
			ticket.puesto=request.POST["puesto"]
			ticket.save()
			return redirect('/tickets/')
	else:
		form = ticketForm()
	return render(request, 'tickets/crear.html', {'form': form})

def actualizar(request, tId):
	template = loader.get_template('tickets/index.html')
	fechaEmision = request.POST.get('fechaEmision')
	ciudadO = request.POST.get('ciudadO')
	ciudadD = request.POST.get('ciudadD')
	precio = request.POST.get('precio')
	cedula = request.POST.get('cedula')
	puesto = request.POST.get('puesto')

	ticket = Ticket.objects.get(id=tId)
	ticket.fechaEmision = fechaEmision
	ticket.ciudadO = ciudadO
	ticket.ciudadD = ciudadD
	ticket.precio = precio
	ticket.cedula = cedula
	ticket.puesto = puesto

	ticket.save()
	context = {}

	return redirect('/tickets/')

def eliminar(request, tId):
	ticket= Ticket.objects.get(pk=tId)
	ticket.delete()
	return redirect('/tickets/')
