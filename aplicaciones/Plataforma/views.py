from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Auto
# Create your views here.

def home(request):
    autoslistados=Auto.objects.all()
    return render(request,"gestionAutos.html",{"autos":autoslistados})

def registrarAuto(request):
    patente=request.POST['txtPatente']
    km=request.POST['numKm']
    precio=request.POST['numPrecio']
    tipo=request.POST['txtTipo']
    disponibilidad=request.POST['txtDisponibilidad']
    auto=Auto.objects.create(patente=patente,km=km,precio=precio,tipo=tipo,disponibilidad=disponibilidad)
    return redirect('/')

def borrarAuto(request,patente):
    auto=Auto.objects.get(patente=patente)
    auto.delete()
    return redirect('/')
def edicionAuto(request,patente):
    auto=Auto.objects.get(patente=patente)
    return render(request,"edicionAuto.html",{'auto':auto})
def editarAuto(request):
    patente=request.POST['txtPatente']
    km=request.POST['numKm']
    precio=request.POST['numPrecio']
    tipo=request.POST['txtTipo']
    disponibilidad=request.POST['txtDisponibilidad']
    auto=Auto.objects.get(patente=patente)
    auto.km=km
    auto.precio=precio
    auto.tipo=tipo
    auto.disponibilidad=disponibilidad
    auto.save()
    return redirect('/')
