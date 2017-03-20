from django.http import HttpResponse
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




