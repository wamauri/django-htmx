from django.test import Client
from django.urls import reverse

from tasks.models import Tasks
from .fixtures import (
    all_tasks, context, tasks_form_data
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