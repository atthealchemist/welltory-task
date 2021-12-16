from fastapi import status

from app.core.config import api_settings

TASKS_ROOT = api_settings.tasks_root


class TestTasksAPI:
    def test_task_list(self, client):
        res = client.get(TASKS_ROOT)
        assert res.status_code == status.HTTP_200_OK
        assert len(res.json()) > 0

    def test_task_create(self, client, task_create_payload):
        res = client.post(f"{TASKS_ROOT}/", json=task_create_payload)
        assert res.status_code == status.HTTP_201_CREATED

    def test_task_get(self, client, fake_tasks_list):
        first, *_ = fake_tasks_list
        first.id = str(first.id)
        res = client.get(f"{TASKS_ROOT}/{first.id}")
        assert res.status_code == status.HTTP_200_OK
        assert res.json() == first.dict()

    def test_task_delete(self, client, fake_tasks_list):
        first, *_ = fake_tasks_list
        res = client.delete(f"{TASKS_ROOT}/{first.id}")
        assert res.status_code == status.HTTP_200_OK
        assert res.json() == {"id": str(first.id), "deleted": True}
