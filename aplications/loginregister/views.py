from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomPasswordChangeForm
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

# Create your views here.

#Vista para modificar los datos del usuario
@login_required
def actualizar_usuario(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Actualiza la sesión de autenticación si se cambió la contraseña
            return redirect('home')  # Redirige a la página de perfil o a donde desees
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'registration/actualizar_usuario.html', {'form': form})

#LOGOUT
def exit (request):
    logout(request)
    return redirect ('home')

#REGISTRO
def register(request):
    data = {
        'form': CustomUserCreationForm()
    }    
    
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm (data=request.POST)
        
        if user_creation_form.is_valid():
            user_creation_form.save()
            
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            
            return redirect('home')
    
    return render (request, 'registration/register.html',data)

#Cambio de contraseña
class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'registration/cambiar-contrasena.html'
    
    
#Cambio de contraseña exitoso
class ContraExitosaPersonalizada(PasswordChangeDoneView):
    template_name = 'registration/cambio-contrasena-exitoso.html'

    def get(self, request):
        # Esta es una vista personalizada para mostrar un mensaje después de cambiar la contraseña
        return super().get(request)


# def cambio_contrasena_exitoso(request):
#     # Realiza el cierre de sesión
#     logout(request)
#     return render(request, 'cambio_contrasena_exitoso.html')