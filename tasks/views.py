from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Tasks


def home(request):
    return render(request, 'base.html')


def get_tasks(done=None):
    if done:
        return Tasks.objects.filter(done=True)
    return Tasks.objects.exclude(done=True)


def build_context():
    return {
        'tasks': get_tasks(),
        'tasks_done': get_tasks(done=True),
    }


def change_task_done(task_id: int, done: bool = False):
    task = Tasks.objects.get(id=task_id)
    task.done = done
    task.save()


@require_http_methods(['GET'])
def tasks(request):
    context = build_context()

    return render(
        request=request, 
        template_name='tasks.html', 
        context=context
    )


@require_http_methods(['POST'])
def create_tasks(request):
    name = request.POST.get('name')
    Tasks.objects.create(name=name)
    context = build_context()

    return render(
        request=request, 
        template_name='tasks.html', 
        context=context
    )


@require_http_methods(['PUT'])
def tasks_done(request, task_id):
    change_task_done(task_id=task_id, done=True)
    context = build_context()

    return render(
        request=request, 
        template_name='tasks.html', 
        context=context
    )


@require_http_methods(['PUT'])
def tasks_undo(request, task_id):
    change_task_done(task_id=task_id)
    context = build_context()

    return render(
        request=request, 
        template_name='tasks.html', 
        context=context
    )


@require_http_methods(['DELETE'])
def tasks_delete(request, task_id):
    Tasks.objects.get(id=task_id).delete()
    context = build_context()

    return render(
        request=request, 
        template_name='tasks.html', 
        context=context
    )
