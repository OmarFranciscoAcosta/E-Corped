from django.shortcuts import redirect, render, get_object_or_404
from .models import Empleado
from .forms import EmpleadoForm
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.


#Render pagina inicio
def home (request):
    return render (request, 'empleado/home.html')
#Publicar empleado
def publicar_empleado(request):
    if request.method == 'POST':
        empleado_form = EmpleadoForm(request.POST, request.FILES)
        if empleado_form.is_valid():
            empleado_form.save()
            # Devuelve una respuesta JSON indicando éxito
            return JsonResponse({'success': True, 'message': 'El empleado ha sido agregado con éxito.'})
        else:
            return JsonResponse({'success': False, 'message': 'Hubo un problema al agregar el empleado.'})
    else:
        empleado_form = EmpleadoForm()
    return render(request, 'empleado/publicar_empleado.html', {'form': empleado_form})

#Buscar empleado
def buscar_empleado(request):
    empleado = None
    if request.method == 'POST':
        # Obtén el término de búsqueda del formulario
        buscar = request.POST.get('buscar')

        # Realiza la búsqueda en la base de datos
        empleado = Empleado.objects.filter(nombre__icontains=buscar).first()

    return render(request, 'empleado/buscar_empleado.html', {'empleado': empleado})

#Listar empleados y mostrarlo por una card.
def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/lista_empleados.html', {'empleados': empleados})

#Formulario de empleados para modificar los datos, cargar una foto nueva y mostrarla por lista_empleados.
def detalles_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    
    if request.method == 'POST':
        if 'editar' in request.POST:
            form = EmpleadoForm(request.POST, request.FILES, instance=empleado)
            if form.is_valid():
                form.save()
                # Redirecciona a la página de lista_empleados después de guardar cambios
                return redirect('empleados')
        elif 'eliminar' in request.POST:
            empleado.delete()
            messages.success(request, 'El empleado ha sido eliminado.')
            return redirect('empleados')  # Redirige a donde desees después de la eliminación
    else:
        form = EmpleadoForm(instance=empleado)
    
    return render(request, 'empleado/detalle_empleado.html', {'form': form, 'empleado': empleado})

#Formulario de acerca de mí.
def about (request):
    return render (request, 'empleado/about.html')

