from django.contrib import admin

# Register your models here.
from .models import Category, Task, Comment

admin.site.register(Category)
admin.site.register(Task)
admin.site.register(Comment)