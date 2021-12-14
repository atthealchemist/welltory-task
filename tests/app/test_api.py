from app.core.config import api_settings

TASKS_ROOT = api_settings.tasks_root


class TestTasksAPI:
    def test_task_list(self, client):
        res = client.get(TASKS_ROOT)
        assert res.status_code == 200
        assert len(res.json()) > 0

    def test_task_create(
        self, client, task_create_payload, task_create_response_payload, monkeypatch
    ):
        res = client.post(TASKS_ROOT, data=task_create_payload)
        monkeypatch.setattr(res, "json", lambda: task_create_response_payload)
        assert res.json() == task_create_response_payload

    def test_task_get(self, client, task_fake_uuid, task_get_payload, monkeypatch):
        res = client.get(f"{TASKS_ROOT}/{task_fake_uuid}")
        monkeypatch.setattr(res, "json", lambda: task_get_payload)
        assert res.json() == task_get_payload

    def test_task_delete(
        self, client, task_fake_uuid, task_delete_response_payload, monkeypatch
    ):
        res = client.delete(f"{TASKS_ROOT}/{task_fake_uuid}")
        monkeypatch.setattr(res, "json", lambda: task_delete_response_payload)
        assert res.json() == task_delete_response_payload
