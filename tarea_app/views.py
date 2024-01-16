from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarea
from .forms import TareaForm


def tarea_list(request):
    tareas = Tarea.objects.all()
    return render(request, 'tarea_list.html', {'tareas': tareas})


def tarea_detail(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    return render(request, 'tarea_detail.html', {'tarea': tarea})


def tarea_nueva(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.save()
            return redirect('tarea_detail', pk=tarea.pk)
    else:
        form = TareaForm()
    return render(request, 'tarea_editar.html', {'form': form})


def tarea_editar(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == "POST":
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.save()
            return redirect('tarea_detail', pk=tarea.pk)
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'tarea_editar.html', {'form': form})


def tarea_eliminar(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    tarea.delete()
    return redirect('tarea_list')
