from django.db import models

# Create your models here.
from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()

    def __str__(self):
        return self.name
