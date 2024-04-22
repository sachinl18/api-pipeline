# 📝 Task Management API with Flask

A simple Flask API for managing tasks! This API provides CRUD operations for tasks and includes Swagger documentation for easy interaction.

## 📂 Folder Structure

```
/swagger-api
|-- 📄 app.py
|-- 🧪 test_app.py
|-- 📋 requirements.txt
|-- 📝 README.md
```

- **📄 `app.py`**: Contains the main Flask application code with API endpoints.
- **🧪 `test_app.py`**: Contains test cases for the API using `pytest`.
- **📋 `requirements.txt`**: Lists all the required Python packages for the project.
- **📝 `README.md`**: Provides detailed information about the project, setup, and usage.

## 🛠️ Prerequisites

- Python 3.x
- pip

## 🚀 Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/liquizar/swagger-api.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd task-api
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## 🏃 Running the API

To run the API, execute:

```bash
python app.py
```

The API will start running on `http://127.0.0.1/`.

## 🧪 Testing the API

To run the test cases, execute:

```bash
pytest
```

## 📚 API Endpoints

### 📋 Get All Tasks

- **URL:** `/tasks`
- **Method:** `GET`
- **Response:** Returns a list of all tasks.

### 📋 Get Task by ID

- **URL:** `/tasks/{task_id}`
- **Method:** `GET`
- **Response:** Returns a specific task by its ID.

### 📋 Create Task

- **URL:** `/tasks`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "title": "Task Title",
        "description": "Task Description",
        "done": false
    }
    ```
- **Response:** Returns the newly created task with an assigned ID.

### 📋 Update Task

- **URL:** `/tasks/{task_id}`
- **Method:** `PUT`
- **Request Body:**
    ```json
    {
        "title": "Updated Task Title",
        "description": "Updated Task Description",
        "done": true
    }
    ```
- **Response:** Returns the updated task.

### 📋 Delete Task

- **URL:** `/tasks/{task_id}`
- **Method:** `DELETE`
- **Response:** Returns a message indicating that the task has been deleted.

### 📘 API Documentation

Swagger documentation is available at:

```
http://127.0.0.1/api-docs
```


