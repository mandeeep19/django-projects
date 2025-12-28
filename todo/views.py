from django.http import HttpResponse
from django.shortcuts import render
from todos.models import Task



def home(request):
    # return HttpResponse("home page")
    uncomplete_tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    context = {
        'tasks': uncomplete_tasks
    }
    # print("Uncomplete Tasks - ",uncomplete_tasks)
    return render(request,'home.html', context)