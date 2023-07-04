from django.urls import path
from . import views

urlpatterns = [
    path('tarea/<int:tarea_id>/', views.detalle_tarea, name='detalle_tarea'),
    path('tarea/<int:tarea_id>/completar/', views.completar_tarea, name='completar_tarea'),
    # Agrega las URLs para crear, editar y eliminar tareas según tus necesidades
]
