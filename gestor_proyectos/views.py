from django.shortcuts import render , redirect, get_object_or_404
from django.http import HttpResponse
from .models import Proyecto, Tarea

def home(request):
    return render(request, 'home.html')


def mostrar_proyectos (request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyectos.html', {'proyectos':proyectos})
    
def nuevos_registros(request):
    
    proyectos = [
    
        Proyecto(nombre="Aplicacion de bancaria", descripcion = "Aplicacion web para gestionar los tramites bancarios ", duracion= 1000),
        Proyecto(nombre="Aplicacion de Mensajeria", descripcion = "Aplicacion web para gestionar los mensajes y llamadas", duracion= 200),
        Proyecto(nombre="Tienda Virtual", descripcion = "Aplicacion web para comprar y vender productos en liena", duracion= 700)
        
        ]
    

    
    for p in proyectos:
        p.save()
    
    return HttpResponse('Registro guardado. ')
    
'''
** EN SQL **
INSERT INTO proyecto (nombre, descripcion, duracion)VALUES
("Aplicacion de biblioteca","Aplicacion web para gestionar los libros y prestamos de la biblioteca", 200)
'''

def ver_proyecto(request, id):
    proyecto= Proyecto.objects.get(id=id)
    return render(request,'detalle-proyecto.html',{'proyecto':proyecto})
   
   
def nuevo_proyecto (request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        duracion = request.POST.get('duracion')
        
        if nombre and descripcion and duracion:
            proyecto = Proyecto(
                nombre = nombre,
                descripcion = descripcion,
                duracion = duracion,
                )
            proyecto.save()
            return redirect('proyectos')
            
    return render(request, 'nuevo-proyecto.html')

'''
def crear_proyecto(request):
    nombre = request.POST.get('nombre')
    descripcion = request.POST.get('descripcion')
    duracion = request.POST.get('duracion')
    
    if nombre and descripcion and duracion:
        proyecto = Proyecto(
            nombre = nombre,
            descripcion = descripcion,
            duracion = duracion,
        )
        proyecto.save()
        return redirect('proyectos')
    
    return render (request, 'nuevo-proyecto.hyml')
'''

def eliminar_proyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    proyecto.delete()
    return redirect('proyectos')
    
    
def editar_proyecto (request,id):
    proyecto = Proyecto.objects.get(id=id)
    
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        duracion = request.POST.get('duracion')
        
        if nombre and descripcion and duracion:
            proyecto.nombre = nombre
            proyecto.descripcion = descripcion
            proyecto.duracion = int(duracion)
            proyecto.save()
            
            return redirect ('ver_proyecto', id= proyecto.id)
    
    return render(request, 'editar-proyecto.html', {'proyecto': proyecto})



def crear_tarea(request, proyecto_id):
    
    proyecto = get_object_or_404(Proyecto, id= proyecto_id)
    
    if request.method == 'POST':
        pass
    
    datos = {
        'proyecyo': proyecto,
        'priodidad_choices': Tarea.PRIORIDAD_CHOICES,
        'estado_choices':Tarea.ESTADO_CHOICES
    }
    
    return render (request, 'crear-tarea.html',datos)