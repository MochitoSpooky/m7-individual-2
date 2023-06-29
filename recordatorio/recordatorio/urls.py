
from django.contrib import admin
from django.urls import path
from tareas.views import CustomLoginView, base, bienvenido
from tareas.views import base, bienvenido
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='base'), name='logout'),
    path('', base, name='base'),
    path('bienvenido/', bienvenido, name='bienvenido'),
]
