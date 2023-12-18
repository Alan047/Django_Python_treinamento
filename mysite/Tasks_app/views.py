from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages

def home(request):
    dados_task = Task.objects.all()
    return render(request, 'Tasks_app/index_tasks_app.html', {"task": dados_task})

def task(request, id_task):
    dados = {

        "TASK" : Task.objects.get(id=id_task).Task,
        "DESC": Task.objects.get(id=id_task).Descricao, 
        "crated_at": Task.objects.get(id=id_task).crated_at,

        }
    
    return render(request, 'Tasks_app/task.html', {"dados" : dados})

def add_task(request):

    if request.method == 'POST':
        form_add_task = TaskForm(request.POST)
        if form_add_task.is_valid():
            form_add_task.save()
            dados = request.POST.get("Task")
            print(dados)
            messages.info(request, f"Tarefa '{dados}' adicionada com sucesso.")
            return redirect('/TasksApp/add_task/')
    else:
        form_add_task = TaskForm()

    return render(request, 'Tasks_app/add_task.html',{"form_add_task":form_add_task})


def edit_task(request, id):
    dado_editar = Task.objects.get(id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=dado_editar)
        if form.is_valid():
            form.save()
            return redirect('/TasksApp/')
            
    else:
        form = TaskForm(instance=dado_editar)
    return render(request, 'Tasks_app/edit_task.html', {'form': form} )


def delete_task(request, id):
    dado = Task.objects.get(id=id)
    dado.delete()
    messages.info(request, 'Tarefa deletada com sucesso.')
    return redirect('/TasksApp/')


