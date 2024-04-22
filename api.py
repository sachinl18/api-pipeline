from flask import Flask, jsonify, request
from flask_swagger import swagger

api = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'Azure Devops',
        'description': 'This API is to help us learn how to implement the Azure DevOps pipeline.',
        'done': False
    },
    {
        'id': 2,
        'title': 'Build API',
        'description': 'Build an API for task management',
        'done': False
    }
]

@api.route('/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    return jsonify(tasks)

@api.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Get a single task by ID"""
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return jsonify(task)
    return jsonify({'message': 'Task not found'}), 404

@api.route('/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    data = request.get_json()
    new_task = {
        'id': len(tasks) + 1,
        'title': data['title'],
        'description': data['description'],
        'done': False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@api.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Update an existing task"""
    task = next((task for task in tasks if task['id'] == task_id), None)
    if not task:
        return jsonify({'message': 'Task not found'}), 404

    data = request.get_json()
    task.update(data)
    return jsonify(task)

@api.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task"""
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': 'Task deleted'}), 200

@api.route('/api-docs')
def api_docs():
    """API documentation"""
    swag = swagger(app)
    swag['info']['title'] = 'Task API'
    swag['info']['version'] = '1.0'
    return jsonify(swag)

if __name__ == '__main__':
    api.run(debug=True)
