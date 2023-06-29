from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'tareas/login.html'  # Ruta al archivo de plantilla de login


def base(request):
    return render(request, 'tareas/base.html')


def bienvenido(request):
    return render(request, 'tareas/bienvenido.html')
