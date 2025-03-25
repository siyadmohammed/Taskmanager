Overview

This project is a Task Management API built with Django and Django REST Framework (DRF). It allows users to create, assign, and manage tasks.


Installation

1.Clone the repository:
		git clone https://github.com/siyadmohammed/Taskmanager.git
		cd task-manager

2.Create a virtual environment:
		python -m venv venv

3.Activate the virtual environment:

		On Windows:
		venv\Scripts\activate

		On macOS/Linux:
		source venv/bin/activate

4.Install the required packages:
		pip install -r requirements.txt

5.Create env file and set the database credentials for configuring postgreSQL:

		DB_NAME=db_name
		DB_USER=db_user
		DB_PASSWORD=db_password
		DB_HOST=db_host(localhost)
		DB_PORT=db_port(5432)

5.Apply migrations:
		python manage.py makemigrations
		python manage.py migrate

6.Create Superuser:
		python manage.py createsuperuser

7.Start the development server:
		python manage.py runserver

The API will be available at http://127.0.0.1:8000/api/.

You can access the Swagger documentation at http://127.0.0.1:8000/swagger

API Endpoints.

     Endpoint			Method		Description
users/				POST		Create a new user
tasks/				POST		Create a new task
tasks/<int:pk>/assign/		POST		Assign a task to one or more users
tasks/<int:pk>/update-status/	PATCH		Update the status of a task
users/<int:user_id>/tasks/	GET		Retrieve tasks assigned to a specific user


Sample API Requests and Responses

1.Create User

Request

text
POST users/
Content-Type: application/json

{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "mobile": "+911234567890",
    "password": "securepassword123"
}

Response

json
{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "mobile": "+911234567890"
}

2.Create Task

Request

text
POST tasks/
Content-Type: application/json

{
    "name": "Complete Report",
    "description": "Prepare the annual financial report.",
    "task_type": "WORK"
}

Response

json
{
    "id": 1,
    "name": "Complete Report",
    "description": "Prepare the annual financial report.",
    "task_type": "WORK",
    "created_at": "2025-03-25T08:34:00Z",
    "status": "PENDING"
}

3.Assign Task to Users

Request

text
POST tasks/1/assign/
Content-Type: application/json

{
    "user_ids": [2, 3]  // List of user IDs to whom the task will be assigned
}

Response

json
{
    "status": "Users assigned successfully"
}

4.Update Task Status

Request

text
PATCH tasks/1/update-status/
Content-Type: application/json

{
    "status": "COMPLETED"
}

Response

json
{
    "id": 1,
    "name": "Complete Report",
    "description": "Prepare the annual financial report.",
    "task_type": "WORK",
    "created_at": "2025-03-25T08:34:00Z",
    "status": "COMPLETED"
}

