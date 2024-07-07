from django.urls import path

from . import views

urlpatterns = [
    path(route='', view=views.tasks, name='tasks'),
    path(route='create', view=views.create_tasks, name='create-tasks')
]
