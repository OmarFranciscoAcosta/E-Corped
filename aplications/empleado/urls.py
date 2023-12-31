"""
URL configuration for empleados project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from .views import home, publicar_empleado, buscar_empleado, lista_empleados, detalles_empleado, about
from django.urls import path


urlpatterns = [
    path('',home, name='home'),
    path('publicar_empleado/', publicar_empleado, name= "publicar_empleado"),
    path('buscar_empleado/', buscar_empleado, name='buscar_empleado'),
    path('empleados/', lista_empleados, name='empleados'),
    path('detalles/<int:empleado_id>/', detalles_empleado, name='detalles'),
    path('about/',about, name='about'),
    
]

