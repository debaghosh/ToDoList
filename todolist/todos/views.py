from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

def todoView(request):
    all_to_do_items = TodoItem.objects.all()
    return render(request, 'todo.html', { 'all_items': all_to_do_items})

def addTodo(request):
    c = request.POST['content']
    new_item = TodoItem(content = c)
    new_item.save()

    return HttpResponseRedirect('/todos/')

def deleteitem(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()


    return HttpResponseRedirect('/todos/')
