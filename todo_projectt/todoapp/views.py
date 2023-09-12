from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from todoapp.form import Todo_Form
from todoapp.models import Todo
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import DeleteView, UpdateView
class List_View(ListView):
        model = Todo
        template_name = 'listview.html'
        context_object_name = 'res'

class Detail_View(DetailView) :
            model = Todo
            template_name = 'detailview.html'
            context_object_name = 'res'


class Delete_View(DeleteView):
            model = Todo
            template_name = 'delete.html'
            success_url = reverse_lazy('todoapp:listview')
class Update_View(UpdateView):
            model = Todo
            template_name = 'edit.html'
            context_object_name = 'res'
            fields = ['task','priority','date']

            def get_success_url(self):
                        return reverse_lazy('detailview',kwargs={'pk':self.object.id})

           # Create your views here.
def home(request):
        obj = Todo.objects.all()
        if request.method == 'POST':
                 task = request.POST['task']
                 priority = request.POST['priority']
                 date = request.POST['date']

                 if task=='' or priority=='' or date=='':
                        messages.info(request,'Empty Fields')

                 elif Todo.objects.filter(priority=priority).exists():
                        messages.info(request,'Priority already taken')
                        return redirect('/')

                 else:
                     todo = Todo(task=task,priority=priority,date=date)
                     todo.save()
                     return redirect('/')

        return render(request,'home.html',{'res':obj})

# def details(request):
#         obj = Todo.objects.all()
#         return render(request,'details.html',{'res':obj})

def delete(request,task_id):
            if request.method== 'POST':
                obj = Todo.objects.get(id=task_id)
                obj.delete()
                return redirect('/')

            return render(request,'delete.html')


def update(request,task_id):
            task = Todo.objects.get(id=task_id)
            form = Todo_Form(request.POST or None,instance=task)

            if form.is_valid():
                    form.save()
                    return redirect('/')

            return render(request,'update.html',{'task':task,'form':form})