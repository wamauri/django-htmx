from django.test import Client
from django.urls import reverse

from tasks.models import Tasks
from .fixtures import (
    all_tasks, context, tasks_form_data,
    task_instace
)


class TestTasksViews:
    def setup_method(self, method):
        self.c = Client()

    def test_home_status_code_200(self):
        url = reverse('home')
        res = self.c.get(url)
        assert res.status_code == 200

    def test_get_all_tasks(self, all_tasks):
        assert len(all_tasks) > 1

    def test_get_tasks_return_tasks_instances(self, all_tasks):
        assert isinstance(all_tasks[0], Tasks)

    def test_build_context_return_a_dict(self, context):
        assert isinstance(context, dict)

    def test_tasks_view_return_status_code_200(self, db):
        url = reverse('tasks')
        res = self.c.get(url)
        assert res.status_code == 200

    def test_post_tasks_create_an_object_tasks(self, tasks_form_data):
        url = reverse('create-tasks')
        res = self.c.post(url, tasks_form_data)
        assert res.status_code == 200

    def test_task_done_view(self, task_instace):
        url = reverse('done-task', kwargs={'task_id': task_instace.id})
        res = self.c.put(url)
        assert res.status_code == 200
        assert res.context[0]['tasks_done'][0].done == True

    def test_task_undo_view(self, task_instace):
        url = reverse('undo-task', kwargs={'task_id': task_instace.id})
        res = self.c.put(url)
        assert res.status_code == 200
        assert res.context[0]['tasks'][0].done == False

    def test_task_delete_view(self, task_instace):
        url = reverse('delete-task', kwargs={'task_id': task_instace.id})
        res = self.c.delete(url)
        assert res.status_code == 200

    def test_get_task_view(self, all_tasks):
        url = reverse('task', kwargs={'task_id': all_tasks[0].id})
        res = self.c.get(url)
        assert res.context[0]['task'].name == 'A'

    def test_task_edit_view(self, all_tasks):
        task_id = all_tasks[0].id
        instance = all_tasks.filter(id=task_id)[0]
        assert instance.name == 'A'

        url = reverse('edit-task', kwargs={'task_id': task_id})
        res = self.c.post(url, data={'name': 'Task Name'})
        assert res.context[0]['tasks'][0].name == 'Task Name'
        assert res.context[0]['tasks'][0].name != 'A'
