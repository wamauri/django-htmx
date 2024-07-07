from django.shortcuts import render


def home(request):
    return render(request, 'base.html')


def tasks(request):
    return render(request, 'tasks.html')
