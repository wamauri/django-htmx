import pytest

from tasks.models import Tasks
from tasks.views import get_tasks, build_context


@pytest.fixture
def all_tasks(db):
    Tasks.objects.bulk_create(
        [
            Tasks(name='A'),
            Tasks(name='B'),
            Tasks(name='C'),
        ]
    )
    return get_tasks()


@pytest.fixture
def context(db):
    return build_context()


@pytest.fixture
def tasks_form_data(db):
    return {'name': 'D'}


@pytest.fixture
def task_instace(db):
    return Tasks.objects.create(name='E')
