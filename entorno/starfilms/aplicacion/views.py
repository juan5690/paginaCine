from django.shortcuts import render, redirect, get_object_or_404
from .models import pelicula, persona
from .forms import *
# Create your views here.

def index(request):
    peliculas = pelicula.objects.all()
    
    data= {
        'peliculas' : peliculas        
    }
    return render(request, 'app/index.html', data)

def compraBoleto(request):
    return render(request, 'app/compraBoleto.html')

def sesion(request):
    return  render(request, 'app/sesion.html')

def jaws(request):
    return render(request, 'app/jaws.html')

def halloween(request):
    return render(request, 'app/halloween.html')

def thedriver(request):
    return render(request, 'app/thedriver.html')

def medioPago(request):
    return render(request, 'app/medioPago.html')

""" personas """

def agregar_persona(request):
    
    data={
        'form':personaForm() 
    }
    
    if request.method =='POST':
        formulario = personaForm(data = request.POST)
        
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="usuario guardado exitosamente!!!"
        else:
            data["form"] = formulario
        
    return render(request, 'app/personas/agregar.html', data)


def listar_personas(request):
    personas = persona.objects.all()
    
    data = {
        'personas': personas
    }
    
    return render(request, 'app/personas/listar.html', data)


def updatepersona(request, id):
    persona_instance = get_object_or_404(persona, rut=id)

    form = frmUpdatePersona(instance=persona_instance)
    contexto = {
        "form": form,
        "persona": persona_instance
    }

    if request.method == "POST":
        form = frmUpdatePersona(data=request.POST, instance=persona_instance)

        if form.is_valid():
            form.save()
            return redirect("listar_personas")

    return render(request, "app/personas/modificar.html", contexto)


def eliminarpersona(request,id):
    personas=get_object_or_404(persona, rut=id)
    personas.delete()
    return redirect(to="listar_personas")



""" peliculas """
def agregar_pelicula(request):
    
    data={
        'form':peliculaForm() 
    }
    
    if request.method =="POST":
        formulario =peliculaForm(data=request.POST, files=request.FILES)
        
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="pelicula guardada exitosamente!!!"
        else:
            data["form"] = formulario
        
    return render(request, 'app/peliculas/agregar.html', data)

def listar_peliculas(request):
    peliculas = pelicula.objects.all
    
    data={
        'pelicula': peliculas
    }
    return render(request, 'app/peliculas/listar.html', data)

def eliminarpelicula(request,id):
    peliculas=get_object_or_404(pelicula, nombrePeli=id)
    peliculas.delete()
    return redirect(to="listar_peliculas")