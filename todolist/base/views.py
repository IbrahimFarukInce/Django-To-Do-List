from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . models import Task

class TaskList(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

class TaskCreate(CreateView):
    model = Task
    fields = "__all__"
    template_name = 'base/task_form.html'
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"
    template_name = 'base/task_form.html'
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model = Task
    fields = "__all__"
    template_name = 'base/task_delete.html'
    success_url = reverse_lazy('tasks')
