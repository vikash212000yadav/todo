from django.db import models
from users.models import User
from django.contrib.auth.models import AbstractUser

class Status(object):
    Waiting = 'WA'
    Working = 'WR'
    Done = 'DN'
    STATUS_CHOICES = [
        (Waiting, 'Waiting'),
        (Working, 'Working'),
        (Done, 'Done'),
    ]


class Todo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    user = models.ForeignKey(User, related_name='todos', on_delete=models.CASCADE)
    #user field is used to represent the user who created the code todos
    description = models.CharField(max_length=250, blank=True, default='')
    status = models.CharField(
        choices=Status.STATUS_CHOICES, max_length=2, default='WA'
    )

    class Meta:
        ordering = ('created',)


