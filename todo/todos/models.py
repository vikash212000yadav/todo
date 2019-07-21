from django.db import models
from users.models import User


class Status(models.Model):
    Waiting = 'WA'
    Working = 'WR'
    Done = 'DN'
    STATUS_CHOICES = [
        (Waiting, 'Waiting'),
        (Working, 'Working'),
        (Done, 'Done'),
    ]
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        blank=False,
        null=False,
        default='Waiting',
    )


class Todo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    user = models.ForeignKey(User, related_name='todos', on_delete=models.CASCADE)
    #user field is used to represent the user who created the code todos
    description = models.CharField(max_length=250, blank=True, default='')
    choice = models.CharField(max_length=10, blank=True, default='Waiting')
    #status = models.ForeignKey(Status, on_delete=models.CASCADE, default='Waiting')
    #action = models.ForeignKey(Status, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)


