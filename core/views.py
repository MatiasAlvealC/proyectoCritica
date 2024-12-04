from django.shortcuts import render, get_object_or_404, redirect
from database.models import Pelicula
from django.core.paginator import Paginator
from django.db.models import Q

def home(request):
  peliculas = Pelicula.objects.all().order_by('-created')  # Ordena por fecha de creación descendente
  paginator = Paginator(peliculas, 12)  # Muestra 12 películas por página
  page_number = request.GET.get("page")
  page_obj = paginator.get_page(page_number)
  return render(request, "core/home.html", {"page_obj": page_obj})


def pelicula_detalles(request, pelicula_id):
  pelicula = get_object_or_404(Pelicula, id=pelicula_id)
  return render(request, "core/pelicula_detalles.html", {"pelicula": pelicula})


def accion_aventura(request):
    peliculas = Pelicula.objects.filter(
        Q(genero__nombre__icontains="Aventura") | Q(genero__nombre__icontains="Accion")
    ).distinct()  # Evita duplicados en caso de múltiples géneros relacionados

    # Implementación de paginación
    paginator = Paginator(peliculas, 9)  # Muestra 9 películas por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "core/accion_aventura.html", {"page_obj": page_obj})


def comedia(request):
    peliculas = Pelicula.objects.filter(genero__nombre__icontains="Comedia").distinct()
    paginator = Paginator(peliculas, 9)  # Mostrar 9 películas por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "core/comedia.html", {"page_obj": page_obj})

def drama(request):
    peliculas = Pelicula.objects.filter(genero__nombre__icontains="Drama").distinct()
    paginator = Paginator(peliculas, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "core/drama.html", {"page_obj": page_obj})

def ciencia_fantasia(request):
    peliculas = Pelicula.objects.filter(
        Q(genero__nombre__icontains="Ciencia Ficción") | Q(genero__nombre__icontains="Fantasía")
    ).distinct()
    paginator = Paginator(peliculas, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "core/ciencia_fantasia.html", {"page_obj": page_obj})

def horror_suspenso(request):
    peliculas = Pelicula.objects.filter(
        Q(genero__nombre__icontains="Terror") | Q(genero__nombre__icontains="Suspenso")
    ).distinct()
    paginator = Paginator(peliculas, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "core/horror_suspenso.html", {"page_obj": page_obj})

def romance(request):
    peliculas = Pelicula.objects.filter(genero__nombre__icontains="Romance").distinct()
    paginator = Paginator(peliculas, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "core/romance.html", {"page_obj": page_obj})

def animacion(request):
    peliculas = Pelicula.objects.filter(genero__nombre__icontains="Animacion").distinct()
    paginator = Paginator(peliculas, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "core/animacion.html", {"page_obj": page_obj})

def documental(request):
    peliculas = Pelicula.objects.filter(genero__nombre__icontains="Documental").distinct()
    paginator = Paginator(peliculas, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "core/documental.html", {"page_obj": page_obj})

  
def nosotros(request):
    return render(request, "core/nosotros.html")

def contacto(request):
    return render(request, "core/contacto.html")
