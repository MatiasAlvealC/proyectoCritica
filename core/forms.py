from django import forms  # Importa las clases necesarias para trabajar con formularios en Django.
from django.contrib.auth.forms import UserCreationForm  # Importa el formulario de creación de usuario de Django.
from django.contrib.auth.models import User, Group  # Importa los modelos User y Group de Django.

class CustomUserCreationForm(UserCreationForm):  # Define un formulario personalizado para la creación de usuario.
    email = forms.EmailField(required=True)  # Define un campo de correo electrónico obligatorio.
    grupo = forms.ModelChoiceField(  # Define un campo de selección para el grupo del usuario.
        queryset=Group.objects.filter(name='EditorPelicula'),  # Filtra los grupos para solo mostrar 'EditorPelicula'.
        required=True,  # Hace que el campo sea obligatorio.
        widget=forms.Select(attrs={  # Define el widget del campo como un selector con estilo personalizado.
            'class': 'form-control',
            'placeholder': 'Seleccione el grupo'
        }),
        label='Grupo de Usuario',  # Etiqueta del campo de selección.
        initial=Group.objects.filter(name='EditorPelicula').first()  # Establece el valor inicial del campo con el primer grupo 'EditorPelicula'.
    )

    class Meta:  # Metadatos del formulario.
        model = User  # Utiliza el modelo User de Django.
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'grupo']  # Campos a mostrar en el formulario.

    def clean_email(self):  # Método para validar que el correo electrónico no esté ya registrado.
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():  # Si ya existe un usuario con el mismo correo.
            raise forms.ValidationError('Este correo electrónico ya está registrado')  # Lanza un error de validación.
        return email

    def save(self, commit=True):  # Método para guardar el usuario después de la validación.
        user = super().save(commit=False)  # Crea el usuario sin guardarlo aún.
        user.is_staff = True  # Hace al usuario miembro del staff (acceso al admin).
        if commit:  # Si se permite guardar, guarda el usuario.
            user.save()
            grupo = self.cleaned_data.get('grupo')  # Obtiene el grupo seleccionado.
            if grupo:  # Si el grupo es válido, agrega al usuario a ese grupo.
                grupo.user_set.add(user)
        return user  # Devuelve el usuario guardado.

def user_login(request):  # Vista para manejar el inicio de sesión.
    if request.method == 'POST':  # Si la solicitud es POST (enviar formulario).
        form = AuthenticationForm(request, data=request.POST)  # Crea un formulario de autenticación.
        if form.is_valid():  # Si el formulario es válido.
            user = form.get_user()  # Obtiene el usuario autenticado.
            login(request, user)  # Inicia sesión para el usuario.
            return redirect('home')  # Redirige a la página de inicio.
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')  # Muestra un mensaje de error si los datos son incorrectos.
    else:
        form = AuthenticationForm()  # Si es una solicitud GET, crea un formulario vacío.
    return render(request, 'registration/login.html', {'form': form})  # Renderiza la plantilla de inicio de sesión con el formulario.
