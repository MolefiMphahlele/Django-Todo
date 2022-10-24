
from django.shortcuts import render
from  .models import Task
from .forms import TaskCreate
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def HomePage(request):
    Todo_list = Task.objects.order_by('-created')
    
    return render(request, 'Todo/Homepage.html', {'TaskList' : Todo_list})

def TaskCreation(request):
    
    if request.method == 'POST':
        form = TaskCreate(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = TaskCreate()
        return render(
                    request, 
                    'Todo/Task_create.html', 
                    {'form' : form}
        )

def TaskUpdate(request, task_id):  

    task_object = Task.objects.get(id=task_id)
    

    if request.method == 'POST': 
        task_form = TaskCreate(request.POST, instance = task_object)       
        if task_form.is_valid():
            task_form.save()
            return HttpResponseRedirect(render(request, "Todo/Homepage"))
    
    else:       
        Form = TaskCreate(instance = task_object)
        return render (
                    request, 
                    'Todo/Task_update.html', 
                    {'task_id': task_id,
                    'task': Form}
        )

def TaskDelete(request, task_id):
    # request from update is a GET, negates intent
    if request.method == 'GET':
        Task.objects.get(id =task_id).delete()
        return HttpResponseRedirect(reverse('home')) 
       
    else:
        return render(request,'Todo/Task_delete.html', {'task': Task.objects.get(id =task_id)})

    
