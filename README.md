# Productivity App - Task Manager

A secure Flask REST API where users can manage their personal tasks.

## Stack
Flask + Flask-RESTful + Flask-SQLAlchemy + Flask-Migrate + Flask-Bcrypt
Session-based authentication
SQLite database

## Installation

### 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/full-auth-flask-backend.git
cd full-auth-flask-backend/productivity-app

### 2. Install dependencies
pipenv install

### 3. Activate virtual environment
pipenv shell

### 4. Run migrations
pipenv run flask db init
pipenv run flask db migrate -m "initial migration"
pipenv run flask db upgrade

### 5. Seed the database
pipenv run python seed.py

### 6. Run the server
pipenv run flask run

## API Endpoints

### Auth
POST /register - Create a new account - No auth required
POST /login - Login and start session - No auth required
DELETE /logout - End current session - No auth required
GET /check_session - Get logged in user - Auth required

### Tasks
GET /tasks - Get your tasks paginated - Auth required
POST /tasks - Create a new task - Auth required
PATCH /tasks/<id> - Update your task - Auth required
DELETE /tasks/<id> - Delete your task - Auth required

## Request Body Examples

### Register / Login
{
    "username": "kaltun",
    "password": "password123"
}

### Create / Update Task
{
    "title": "My task",
    "description": "Task description"
}

### Mark Task Complete
{
    "completed": true
}

## Pagination
GET /tasks?page=1

## Test Users
username: kaltun | password: password123
username: abdullahi | password: password123
username: sahal | password: password123