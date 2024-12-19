from django.shortcuts import render, get_object_or_404, redirect  # Funciones para renderizar vistas, obtener objetos o redirigir a otras páginas.
from database.models import Pelicula  # Modelo Pelicula desde la base de datos.
from django.core.paginator import Paginator  # Función para implementar la paginación de los resultados.
from django.db.models import Q  # Para realizar búsquedas con condiciones OR entre campos.
from django.contrib.auth.forms import UserCreationForm  # Formulario para la creación de usuarios predeterminado de Django.
from django.contrib import messages  # Para mostrar mensajes al usuario.
from django.contrib.auth import authenticate, login  # Funciones para autenticar y loguear a un usuario.
from .forms import CustomUserCreationForm  # Formulario personalizado para la creación de usuarios.
from django.contrib.auth.forms import AuthenticationForm  # Formulario para la autenticación de usuarios.
from django.contrib.auth.decorators import login_required  # Decorador para proteger vistas que requieren estar autenticado.
from django.urls import reverse
from .forms import contactForm
from django.core.mail import EmailMessage

# Vista para la página de inicio mostrando las últimas películas en orden descendente por fecha de creación.
def home(request):
    peliculas = Pelicula.objects.all().order_by('-created')  # Ordena las películas por fecha de creación de forma descendente.
    paginator = Paginator(peliculas, 12)  # Muestra 12 películas por página.
    page_number = request.GET.get("page")  # Obtiene el número de página desde la URL.
    page_obj = paginator.get_page(page_number)  # Paginación de las películas.
    return render(request, "core/home.html", {"page_obj": page_obj})  # Renderiza la vista con las películas.

# Vista para los detalles de una película.
def pelicula_detalles(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, id=pelicula_id)  # Obtiene la película por su ID o devuelve 404 si no se encuentra.
    comentarios = pelicula.comentarios.all()  # Obtiene los comentarios asociados a la película.
    return render(request, "core/pelicula_detalles.html", {
        "pelicula": pelicula,  # Pasa la película.
        "comentarios": comentarios  # Pasa los comentarios de la película.
    })

# Vista protegida para que los usuarios autenticados puedan comentar sobre una película.
@login_required
def comentar(request, pelicula_id):
    if request.method == "POST":
        pelicula = get_object_or_404(Pelicula, id=pelicula_id)  # Obtiene la película por su ID.
        texto = request.POST.get("texto", "").strip()  # Obtiene el texto del comentario.
        if texto:  # Si el comentario no está vacío.
            Comentario.objects.create(  # Crea un nuevo comentario.
                pelicula=pelicula,
                usuario=request.user,  # Usuario autenticado que hace el comentario.
                texto=texto
            )
        return redirect('pelicula_detalles', pelicula_id=pelicula.id)  # Redirige a la página de detalles de la película.

# Vista para mostrar películas de las categorías Acción y Aventura.
def accion_aventura(request):
    peliculas = Pelicula.objects.filter(
        Q(genero__nombre__icontains="Aventura") | Q(genero__nombre__icontains="Accion")
    ).distinct()  # Filtra por películas de géneros Acción o Aventura.
    paginator = Paginator(peliculas, 9)  # Paginación de 9 películas por página.
    page_number = request.GET.get("page")  # Obtiene el número de página desde la URL.
    page_obj = paginator.get_page(page_number)  # Paginación de las películas.
    return render(request, "core/accion_aventura.html", {"page_obj": page_obj})  # Renderiza la vista de Acción/Aventura.

# Vista para mostrar películas de la categoría Comedia.
def comedia(request):
    peliculas = Pelicula.objects.filter(genero__nombre__icontains="Comedia").distinct()  # Filtra películas de Comedia.
    paginator = Paginator(peliculas, 9)  # Paginación de 9 películas por página.
    page_number = request.GET.get("page")  # Obtiene el número de página desde la URL.
    page_obj = paginator.get_page(page_number)  # Paginación de las películas.
    return render(request, "core/comedia.html", {"page_obj": page_obj})  # Renderiza la vista de Comedia.

# Vista para mostrar películas de la categoría Drama.
def drama(request):
    peliculas = Pelicula.objects.filter(genero__nombre__icontains="Drama").distinct()  # Filtra películas de Drama.
    paginator = Paginator(peliculas, 9)  # Paginación de 9 películas por página.
    page_number = request.GET.get("page")  # Obtiene el número de página desde la URL.
    page_obj = paginator.get_page(page_number)  # Paginación de las películas.
    return render(request, "core/drama.html", {"page_obj": page_obj})  # Renderiza la vista de Drama.

# Vista para mostrar películas de Ciencia Ficción y Fantasía.
def ciencia_fantasia(request):
    peliculas = Pelicula.objects.filter(
        Q(genero__nombre__icontains="Ciencia Ficción") | Q(genero__nombre__icontains="Fantasía")
    ).distinct()  # Filtra películas de Ciencia Ficción o Fantasía.
    paginator = Paginator(peliculas, 9)  # Paginación de 9 películas por página.
    page_number = request.GET.get("page")  # Obtiene el número de página desde la URL.
    page_obj = paginator.get_page(page_number)  # Paginación de las películas.
    return render(request, "core/ciencia_fantasia.html", {"page_obj": page_obj})  # Renderiza la vista de Ciencia Ficción/Fantasía.

# Vista para mostrar películas de Terror y Suspenso.
def horror_suspenso(request):
    peliculas = Pelicula.objects.filter(
        Q(genero__nombre__icontains="Terror") | Q(genero__nombre__icontains="Suspenso")
    ).distinct()  # Filtra películas de Terror o Suspenso.
    paginator = Paginator(peliculas, 9)  # Paginación de 9 películas por página.
    page_number = request.GET.get("page")  # Obtiene el número de página desde la URL.
    page_obj = paginator.get_page(page_number)  # Paginación de las películas.
    return render(request, "core/horror_suspenso.html", {"page_obj": page_obj})  # Renderiza la vista de Terror/Suspenso.

# Vista para mostrar películas de Romance.
def romance(request):
    peliculas = Pelicula.objects.filter(genero__nombre__icontains="Romance").distinct()  # Filtra películas de Romance.
    paginator = Paginator(peliculas, 9)  # Paginación de 9 películas por página.
    page_number = request.GET.get("page")  # Obtiene el número de página desde la URL.
    page_obj = paginator.get_page(page_number)  # Paginación de las películas.
    return render(request, "core/romance.html", {"page_obj": page_obj})  # Renderiza la vista de Romance.

# Vista para mostrar películas de Animación.
def animacion(request):
    peliculas = Pelicula.objects.filter(genero__nombre__icontains="Animacion").distinct()  # Filtra películas de Animación.
    paginator = Paginator(peliculas, 9)  # Paginación de 9 películas por página.
    page_number = request.GET.get("page")  # Obtiene el número de página desde la URL.
    page_obj = paginator.get_page(page_number)  # Paginación de las películas.
    return render(request, "core/animacion.html", {"page_obj": page_obj})  # Renderiza la vista de Animación.

# Vista para mostrar películas de Documentales.
def documental(request):
    peliculas = Pelicula.objects.filter(genero__nombre__icontains="Documental").distinct()  # Filtra películas de Documental.
    paginator = Paginator(peliculas, 9)  # Paginación de 9 películas por página.
    page_number = request.GET.get("page")  # Obtiene el número de página desde la URL.
    page_obj = paginator.get_page(page_number)  # Paginación de las películas.
    return render(request, "core/documental.html", {"page_obj": page_obj})  # Renderiza la vista de Documentales.

# Vista para la página "Nosotros".
def nosotros(request):
    return render(request, "core/nosotros.html")  # Renderiza la página "Nosotros".

# Vista para la página de contacto.
def contacto(request):
    contact_form = contactForm() # se captura el formulario
    if request.method == "POST": # si algo viajo por el metodo POST
        contact_form = contactForm(data=request.POST) # se incluyen los valores enviados a el objeto contact_form
        if contact_form.is_valid(): # si lo camputarado en contact_form es valido se le entragaran a los siguientes objetos:
            name = request.POST.get('name','') 
            email = request.POST.get('email','')
            message = request.POST.get('message','')

            # se arma el email
            email = EmailMessage(
                'Mensaje de contacto recibido',
                'Mensaje enviado por {} <{}>: \n\n{}'.format(name,email,message), email,
                ['f7642f16bcf916@inbox.mailtrap.io'],reply_to=[email], #esto envia a una lita de correo, pero nosotros solo tenemos mailtrap configurado
            )

            try:
                email.send() #aqui se envia
                # esta todo ok
                return redirect(reverse('contacto')+'?ok')
            except:
                # ha habido un error y retorno a ERROR
                return redirect(reverse('contacto')+'?error')

    return render(request, "core/contacto.html", {'form':contact_form})  # Renderiza la página de Contacto.

# Vista para el registro de usuarios.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Crea un formulario personalizado para la creación de usuarios.
        if form.is_valid():  # Si el formulario es válido.
            form.save()  # Guarda el nuevo usuario.
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')  # Mensaje de éxito.
            return redirect('login')  # Redirige a la página de inicio de sesión.
    else:
        form = CustomUserCreationForm()  # Si no es un POST, crea un formulario vacío.
    return render(request, 'registration/register.html', {'form': form})  # Renderiza la página de registro con el formulario.

# Vista para el inicio de sesión de usuarios.
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)  # Obtiene los datos del formulario de autenticación.
        if form.is_valid():  # Si el formulario es válido.
            username = form.cleaned_data.get('username')  # Obtiene el nombre de usuario.
            password = form.cleaned_data.get('password')  # Obtiene la contraseña.
            user = authenticate(request, username=username, password=password)  # Autentica al usuario.
            if user is not None:  # Si el usuario es válido.
                login(request, user)  # Inicia sesión.
                return redirect('home')  # Redirige a la página de inicio.
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')  # Mensaje de error.
    else:
        form = AuthenticationForm()  # Si no es un POST, crea un formulario vacío.
    return render(request, 'registration/login.html', {'form': form})  # Renderiza la página de inicio de sesión con el formulario.
