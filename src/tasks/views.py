from django.shortcuts import render,redirect
from  .models import Todo

from .forms import TodoForm


def home(request):
    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            form = TodoForm()

    todo = Todo.objects.all()
    
    context = {
        "form":form,
        "todo": todo

    }
        
    return render(request,"tasks/task.html",context)

# Delete 
def delete_todo(request, id):
    # fetch the object related to passed id
    task = Todo.objects.get(pk=id)
    print(task)
    task.delete()
    return redirect('home')

def edit_todo(request, id):
     # fetch the object related to passed id
    task = Todo.objects.get(pk=id)
    form = TodoForm(request.POST or None, instance = task)

    if form.is_valid():
        form.save()
        return redirect("home")

    context={
       'form':form
    }

    return render(request,'tasks/edit.html', context)







