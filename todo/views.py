from django.urls import reverse_lazy
from django.views import generic
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect

from todo.forms import TaskForm
from todo.models import Task


def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.toggle_status()
    return redirect("todo:index")


class IndexView(generic.ListView):
    model = Task
    paginate_by = 3
    template_name = "todo/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_date"] = timezone.now()
        return context


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")
