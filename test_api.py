import pytest
import json
from api import api, tasks

@pytest.fixture
def client():
    api.config['TESTING'] = True
    with api.test_client() as client:
        yield client

def test_get_tasks(client):
    response = client.get('/tasks')
    assert response.status_code == 200
    assert len(response.json) == len(tasks)

def test_get_task(client):
    response = client.get('/tasks/1')
    assert response.status_code == 200
    assert response.json['id'] == 1

def test_get_nonexistent_task(client):
    response = client.get('/tasks/100')
    assert response.status_code == 404
    assert 'Task not found' in response.json['message']

def test_create_task(client):
    new_task = {
        'title': 'Test Task',
        'description': 'This is a test task',
        'done': False
    }
    response = client.post('/tasks', json=new_task)
    assert response.status_code == 201
    assert 'id' in response.json
    assert response.json['title'] == new_task['title']

def test_update_task(client):
    updated_task = {
        'title': 'Updated Task',
        'description': 'This is an updated task',
        'done': True
    }
    response = client.put('/tasks/1', json=updated_task)
    assert response.status_code == 200
    assert response.json['title'] == updated_task['title']
    assert response.json['description'] == updated_task['description']
    assert response.json['done'] == updated_task['done']

def test_update_nonexistent_task(client):
    updated_task = {
        'title': 'Updated Task',
        'description': 'This is an updated task',
        'done': True
    }
    response = client.put('/tasks/100', json=updated_task)
    assert response.status_code == 404
    assert 'Task not found' in response.json['message']

def test_delete_task(client):
    response = client.delete('/tasks/1')
    assert response.status_code == 200
    assert 'Task deleted' in response.json['message']
