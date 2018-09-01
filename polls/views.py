from django.shortcuts import render, redirect
from django.http import HttpResponse
from polls.forms import add_proveedoresform, add_licitacionesform
from django.contrib import messages
from polls.models import proveedor, licitaciones


def index(request):
    return render(request, 'index.html')


def add_proveedores(request):
	if request.method == 'POST':
		form = add_proveedoresform(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Se creo el Proveedor!')
			return redirect('index')
		else:
			messages.warning(request, 'Completa bien los datos GATO')
			return render(request, 'proveedores/add_proveedores.html', {'form':form}) 
	else:
		form = add_proveedoresform()
	return render(request, 'proveedores/add_proveedores.html', {'form':form})

def add_licitaciones(request):
	if request.method == 'POST':
		form = add_licitacionesform(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Se creo la licitacion!')
			return redirect('index')
		else:
			messages.warning(request, 'Completa bien los datos GATO')
			return render(request, 'licitaciones/add_licitaciones.html', {'form':form}) 
	else:
		form = add_licitacionesform()
	return render(request, 'licitaciones/add_licitaciones.html', {'form':form})

def list_proveedores(request):
	list_proveedores = proveedor.objects.all()
	return render(request, 'proveedores/list_proveedores.html', {'list_proveedores':list_proveedores})


def list_licitaciones(request):
	list_licitaciones = licitaciones.objects.all()
	return render(request, 'licitaciones/list_licitaciones.html', {'list_licitaciones':list_licitaciones})