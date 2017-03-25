from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render

from tasks.models import Task


def task_list(request):
    """"
    Recupera todas las tareas de la base de datos y las pimta
    :param request:HttpRequest
    :return HttpResponse
    """
    # recuperamos los objs del modelo
    tasks = Task.objects.select_related("owner", "assigned")

    #devolvemos la respuesta
    context = {
        'task_objects': tasks
    }

    return render(request, 'task/list.html', context)

def task_detail(request,task_pk):
    """
    Recupera una tarea de la BBDD y la pinta con una plantilla
    :param request: HttpRequest
    :param task_pk: Primary key de la tarea a recuperar
    :return: HttpResponse
    """

    #recuperar la tarea
    #tenemos 2 formas: forma 1=> try y excepts, forma 2: if-else controlando el num de elementos
    try:
        task = Task.objects.get(pk=task_pk)
    except Task.DoesNotExist:
        return HttpResponseNotFound("la tarea no existe")
    except Task.MultipleObjectsReturned:
        return HttpResponse("Existen varias tareas con ese id", status=300)

    #preparar el contexto
    context = {
        'task': task
    }

    #renderizar la plantilla
    return render(request, 'task/detail.html', context)