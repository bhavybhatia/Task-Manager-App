from django.shortcuts import render
from .models import taskItem
from django.http import HttpResponseRedirect


# def viewTask(request):
#     all_tasks=taskItem.objects.all()
#     return render(request, "task.html",{'all_tasks':all_tasks})
#
# def addTask(request):
#     new_item=taskItem(content=request.POST['content'])
#     new_item.save()
#     return HttpResponseRedirect('/task/')
def home(request):
    if request.method=='POST':
        new_item=taskItem(content=request.POST['content'])
        new_item.save()
        return HttpResponseRedirect('/home/')
    else:
        all_tasks=taskItem.objects.all()
        return render(request, "task.html",{'all_tasks':all_tasks})

def deleteTask(request,todo_id):
    delete_item=taskItem.objects.get(id=todo_id)
    delete_item.delete()
    return HttpResponseRedirect('/home/')
