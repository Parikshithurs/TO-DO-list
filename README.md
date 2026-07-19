# TO-DO List

A simple full-stack To-Do List application built to learn backend development fundamentals and the interaction between a frontend, backend, and database.

## Features

* Add tasks
* View tasks
* Update tasks
* Delete tasks
* Mark tasks as completed

## Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** FastAPI
* **Database:** PostgreSQL

## Run the Project

1. Install the required packages:

```bash
pip install -r backend/requirements.txt
```

2. Create a PostgreSQL database.

3. Start the backend:

```bash
uvicorn backend.main:app --reload
```

4. Open `frontend/index.html` in your browser.

## API Endpoints

* `GET /tasks`
* `GET /tasks/{id}`
* `POST /tasks`
* `PUT /tasks/{id}`
* `DELETE /tasks/{id}`

## Author

**Parikshith Urs**
