from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required

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