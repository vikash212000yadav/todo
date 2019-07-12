from django.db import models

# Create your models here.

class Todo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    class Meta:
        ordering = ('created',)
