from cgitb import html
from pickle import LIST
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView
from .models import Empleado
from .forms import EmpleadosForm
# Create your views here.


#Render pagina inicio
def home (request):
    return render (request, 'empleado/home.html')
#Publicar empleado
def publicar_empleado(request):
    empleado_form = EmpleadosForm()
    
    if request.method == 'POST':
        empleado_form = EmpleadosForm(data=request.POST)
        if empleado_form.is_valid():
            empleado_form.save()
            return redirect('empleado/home.html')  # Redirige a la página de inicio
    else:
        empleado_form = EmpleadosForm()
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