from django.shortcuts import render
from django.http import HttpResponse
from todos.models import Task
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.db import transaction

# Create your views here.

@require_POST
def add_task(request):
    task = request.POST.get('task','').strip()
    if not task:
        print("Task is empty!")
        return redirect('home')
    
    try:
        with transaction.atomic():
            Task.objects.create(task=task)
            print("New Task created successfully!")
    except Exception as e:
        print(f"Err occured while adding task in db - {str(e)}")
    
    return redirect('home')
    
    # result = Task.objects.create(task=task)
    # print(f"result - {result}")
    # return render(request, 'home.html')
    # return redirect('home')


