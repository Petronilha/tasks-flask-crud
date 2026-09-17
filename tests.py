import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'
tasks = []

# Test of create task
def test_create_task():
  new_task_data = {
    "title": "Nova tarefa",
    "description": "descricao da nova tarefa"
  }
  
  response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
  assert response.status_code == 200
  response_json = response.json()
  assert "message" in response_json
  assert "id" in response_json
  tasks.append(response_json['id'])

# test of read tasks
def test_read_tasks():
  response = requests.get(f"{BASE_URL}/tasks")
  assert response.status_code == 200
  response_json = response.json()
  assert "tasks" in response_json
  assert "total_tasks" in response_json

# Test of read specific task
def test_get_task():
  if tasks:
    task_id = tasks[0]
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200
    response_json = response.json()
    assert task_id == response_json['id']

# Test of update specific task
def test_update_task():
  if tasks:
    task_id = tasks[0]
    payload = {
            "completed": True,
            "description": "Nova Descrição",
            "title": "Titulo atualizado"
    }
    
    response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
    response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    
    # Nova requisição a tarefa específica
    response_get = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response_get.status_code == 200
    response_json_get = response_get.json()
    assert response_json_get["title"] == payload["title"]
    assert response_json_get["description"] == payload["description"]
    assert response_json_get["completed"] == payload["completed"]


def test_delete_task():
  if tasks:
    task_id = tasks[0]
    response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    response.status_code == 200

    response_get = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response_get.status_code == 404