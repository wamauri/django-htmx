from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Tasks


def home(request):
    return render(request, 'base.html')


def get_tasks():
    return Tasks.objects.all()


def build_context():
    return {
        'tasks': get_tasks(),
        'bg': 'primary',
    }


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
