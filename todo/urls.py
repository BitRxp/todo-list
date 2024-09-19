from django.urls import path

from .views import (
    IndexView,
    TaskCreateView
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
]

app_name = "todo_list"
