from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Category, Task

def home(request):
    categories = Category.objects.all()
    tasks = Task.objects.all()
    context = {
        'categories': categories,
        'tasks': tasks,
    }
    return render(request, 'main/home.html', context)
