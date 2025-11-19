from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_list_tasks_returns_tasks_array():
    response = client.get("/tasks")
    assert response.status_code == 200
    data = response.json()
    assert "tasks" in data
    assert isinstance(data["tasks"], list)
