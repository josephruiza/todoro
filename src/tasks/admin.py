from django.contrib import admin

from tasks.models import Task

#Registramos el modelo
admin.site.register(Task)
