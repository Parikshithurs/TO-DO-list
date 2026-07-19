from fastapi import FastAPI
from database import get_connection
from schemas import TaskCreate
from fastapi import FastAPI, HTTPException
from schemas import TaskCreate, TaskUpdate
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Fine for learning. Restrict in production.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

@app.get("/tasks")
def get_tasks():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM tasks")

    rows = cursor.fetchall()

    tasks = []

    for row in rows:
        tasks.append({
            "id": row[0],
            "title": row[1],
            "completed": row[2],
            "created_at": row[3]
        })

    cursor.close()
    connection.close()

    return tasks

@app.post("/tasks")
def create_task(task: TaskCreate):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO tasks(title)
        VALUES(%s)
        """,
        (task.title,)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return {
        "message": "Task created successfully"
    }

@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM tasks WHERE id = %s",
        (task_id,)
    )

    task = cursor.fetchone()

    cursor.close()
    connection.close()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task



@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE tasks
        SET title = %s,
            completed = %s
        WHERE id = %s
        """,
        (
            task.title,
            task.completed,
            task_id
        )
    )

    connection.commit()

    if cursor.rowcount == 0:
        cursor.close()
        connection.close()
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    cursor.close()
    connection.close()

    return {
        "message": "Task updated successfully"
    }



@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM tasks
        WHERE id = %s
        """,
        (task_id,)
    )

    connection.commit()

    if cursor.rowcount == 0:
        cursor.close()
        connection.close()

        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    cursor.close()
    connection.close()

    return {
        "message": "Task deleted successfully"
    }