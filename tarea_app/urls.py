from django.urls import path
from .views import tarea_list, tarea_detail, tarea_nueva, tarea_editar, tarea_eliminar

urlpatterns = [
    path('', tarea_list, name='tarea_list'),
    path('tarea/<int:pk>/', tarea_detail, name='tarea_detail'),
    path('tarea/nueva/', tarea_nueva, name='tarea_nueva'),
    path('tarea/<int:pk>/editar/', tarea_editar, name='tarea_editar'),
    path('tarea/<int:pk>/eliminar/', tarea_eliminar, name='tarea_eliminar'),
]
