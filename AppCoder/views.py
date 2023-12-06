from datetime import date

from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

from datetime import datetime
from . import models
from .models import Curso, Profesor

from .forms import CursoFormulario, CursoBuscarFormulario, ProfesorFormulario


def inicio_view(request):
    return render(request, "AppCoder/inicio.html")


def cursos_buscar_view(request):
    if request.method == "GET":
        form = CursoBuscarFormulario()
        return render(
            request,
            "AppCoder/curso_formulario_busqueda.html",
            context={"form": form}
        )
    else:
        formulario = CursoBuscarFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            cursos_filtrados = []
            for curso in Curso.objects.filter(curso=informacion["curso"]):
                cursos_filtrados.append(curso)

            contexto = {"cursos": cursos_filtrados}
            return render(request, "AppCoder/cursos_list.html", contexto)


def cursos_todos_view(request):
    todos_los_cursos = []
    for curso in Curso.objects.all():
        todos_los_cursos.append(curso)

    contexto = {"cursos": todos_los_cursos}
    return render(request, "AppCoder/cursos_list.html", contexto)


def cursos_view(request):
    if request.method == "GET":
        print("+" * 90) #  Imprimimos esto para ver por consola
        print("+" * 90) #  Imprimimos esto para ver por consola
        form = CursoFormulario()
        return render(
            request,
            "AppCoder/curso_formulario_avanzado.html",
            context={"form": form}
        )
    else:
        formulario = CursoFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = Curso(curso=informacion["curso"], camada=informacion["camada"])
            modelo.save()

        return redirect("AppCoder:inicio")


def profesores_view(xx):
    nombre = "Mariano Manuel"
    apellido = "Barracovich"
    ahora = datetime.now()
    diccionario = {
        'nombre': nombre,
        'apellido': apellido,
        "nacionalidad": "argentino",
        "hora": ahora,
        "ciudades_preferidas": ["Buenos Aires", "Lima", "San Pablo", "Trieste"]
    }  # Para enviar al contexto
    return render(xx, "AppCoder/padre.html", diccionario)

def lista_profesores(req):

    profesores = Profesor.objects.all()

    return render(req, "AppCoder/leerProfesores.html", {"lista_profesores": profesores})

def crea_profesor(req):

    if req.method == 'POST':
        miFormulario = ProfesorFormulario(req.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            profesor = Profesor(nombre=data["nombre"], email=data["email"])
            profesor.save()

            return redirect("AppCoder:inicio")
        
        return render(req, "AppCoder/profesorFormulario.html", {"miFormulario": miFormulario})

    else:

        miFormulario = ProfesorFormulario()

        return render(req, "AppCoder/profesorFormulario.html", {"miFormulario": miFormulario})

def eliminar_profesor(req, id):

    if req.method == 'POST':

        profesor = Profesor.objects.get(id=id)
        profesor.delete()

        profesores = Profesor.objects.all()

        return render(req, "AppCoder/leerProfesores.html", {"lista_profesores": profesores})

def editar_profesor(req, id):

    profesor = Profesor.objects.get(id=id)

    if req.method == 'POST':
        miFormulario = ProfesorFormulario(req.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data

            profesor.nombre = data["nombre"]
            profesor.email = data["email"]
            profesor.save()

            return redirect("AppCoder:inicio")
        
        return render(req, "AppCoder/editarProfesor.html", {"miFormulario": miFormulario})

    else:

        miFormulario = ProfesorFormulario(initial={
            "nombre": profesor.nombre,
            "email": profesor.email
        })

        return render(req, "AppCoder/editarProfesor.html", {"miFormulario": miFormulario, "id": profesor.id})    

class CursoList(ListView):

    model = Curso
    template_name = 'AppCoder/curso_list.html'
    context_object_name = "cursos"    

class CursoDetail(DetailView):

    model = Curso
    template_name = 'AppCoder/curso_detail.html'
    context_object_name = "curso"

class CursoCreate(CreateView):

    model = Curso
    template_name = 'AppCoder/curso_create.html'
    fields = ["curso", "camada"]
    success_url = "/AppCoder/cursos/todos"

class CursoUpdate(UpdateView):

    model = Curso
    template_name = 'AppCoder/curso_update.html'
    fields = ["curso", "camada"]
    success_url = "/AppCoder/cursos/todos"

class CursoDelete(DeleteView):

    model=Curso
    template_name = 'AppCoder/curso_delete.html'
    success_url = "/AppCoder/cursos/todos"
