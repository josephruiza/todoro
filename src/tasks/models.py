from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    PENDING = "PEN"
    DONE = "DON"
    STATUSES = (
        (PENDING, "Pending"),
        (DONE, "Done")
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=3, default=PENDING, choices=STATUSES)
    time_estimated = models.IntegerField(blank=True,null=True)
    deadline = models.DateTimeField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True) #automaticamente añada la fecha de creación
    modified_at = models.DateTimeField(auto_now=True) #automaticamente actualiza la fecha
    owner = models.ForeignKey(User, related_name="own_tasks")
    assigned = models.ForeignKey(User, related_name="assigned_tasks", null=True, default=None)

    def __str__(self):
        return self.name
