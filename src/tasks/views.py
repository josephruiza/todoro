from django.http import HttpResponse
from django.shortcuts import render

from tasks.models import Task


def task_list(request):
    """"
    Recupera todas las tareas de la base de datos y las pimta
    :param request:HttpRequest
    :return HttpResponse
    """
    #recuperamos los objs del modelo
    tasks = Task.objects.all()

    #creamos el texto a mostrar
    html = "<ul>"
    for task in tasks:
        html += "<li>" + task.name + "</li>"

    html += "</ul>"

    #devolvemos la respuesta
    return HttpResponse(html)




