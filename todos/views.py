from django.shortcuts import render
from django.http import HttpResponse
from todos.models import Task
from django.shortcuts import redirect, get_object_or_404
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


def mark_as_done(reqeust, pk):
    try:
        with transaction.atomic():
            got_task = get_object_or_404(Task, pk=pk)
            got_task.is_completed = True
            got_task.save()
    except Exception as e:
        print(f"Err occured while marking the task as done - {str(e)}")
    return redirect('home')


def mark_as_undone(request, pk):
    try:
        with transaction.atomic():
            got_task = get_object_or_404(Task, pk=pk)
            got_task.is_completed = False
            got_task.save()
        print("task is marked as undone")
    except Exception as e:
         print(f"Err occured while marking the task as done - {str(e)}")
    return redirect('home')


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        task.task = new_task
        task.save()
        return redirect('home')
    else:
        context= {
            'task': task
        }
    return render(request, 'edit_task.html',context)

def delete_task(reqeust, pk):
    try:
        with transaction.atomic():
            task = get_object_or_404(Task,pk=pk)
            task.delete()
            return redirect('home')
    except Exception as e:
        print(f"Err occurred while deleting the task - {str(e)}")
        return redirect('home')
