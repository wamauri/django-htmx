from .fixtures import (
    task_instace
)

class TestTasksModel:
    def test_tasks_model_str_method(self, task_instace):
        assert str(task_instace) == 'E'
