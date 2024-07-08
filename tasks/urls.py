from django.urls import path

from . import views

urlpatterns = [
    path(
        route='', 
        view=views.tasks, 
        name='tasks'
    ),
    path(
        route='create', 
        view=views.create_tasks, 
        name='create-tasks'
    ),
    path(
        route='done/<int:task_id>/', 
        view=views.tasks_done, 
        name='done-task'
    ),
    path(
        route='delete/<int:task_id>/', 
        view=views.tasks_delete, 
        name='delete-task'
    ),
    path(
        route='undo/<int:task_id>/', 
        view=views.tasks_undo, 
        name='undo-task'
    ),
]
