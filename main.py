from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

# This file creates a small REST API for managing tasks.
# FastAPI automatically turns Python functions into HTTP endpoints.

# Pydantic models define the shape of the incoming JSON request body.
# They also validate the data before it reaches the endpoint.
class TaskCreate(BaseModel):
    # A task must include a title when creating it.
    title: str = Field(..., min_length=3, max_length=100)


class TaskUpdate(BaseModel):
    # When updating a task, both the title and completion status are required.
    title: str
    completed: bool

class TaskPatch(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool

# Create the FastAPI app instance.
# This object is used to register routes and run the API.
app = FastAPI()

# In-memory data storage for the demo app.
# This list is temporary and resets when the server restarts.
tasks = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "completed": False,
    },
    {
        "id": 2,
        "title": "Learn REST",
        "completed": True,
    },
]


# GET request at the root URL.
# This is a simple health or welcome endpoint.
@app.get("/")
def root():
    return {"message": "Hello FastAPI"}


# GET /tasks
# Returns every task currently stored in memory.
# @app.get("/tasks")
# def get_tasks():
#     return tasks
@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks():
    return tasks

# GET /tasks?completed=true
# This route is meant to return only completed tasks.
@app.get("/tasks")
def get_tasks(completed: Optional[bool] = None):

    if completed is None:
        return tasks

    filtered_tasks = []

    for task in tasks:
        if task["completed"] == completed:
            filtered_tasks.append(task)

    return filtered_tasks

# GET /tasks/completed
# This route is meant to return only completed tasks.
@app.get("/tasks/completed")
def get_completed_tasks():
    completed_tasks = []
    for task in tasks:
        if task["completed"]:
            completed_tasks.append(task)
    return completed_tasks


# GET /tasks/{task_id}
# Finds one task by its unique numeric id.
@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    return {"message": "Task not found"}



# POST /tasks
# Creates a new task from the request body.
@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "completed": False
    }

    tasks.append(new_task)

    return new_task


# PUT /tasks/{task_id}
# Replaces the existing task data for that id.
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate):
    for item in tasks:
        if item["id"] == task_id:
            item["title"] = task.title
            item["completed"] = task.completed

            return item

    return {"message": "Task not found"}


# DELETE /tasks/{task_id}
# Removes a task from the in-memory list.
@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return

    raise HTTPException(status_code=404,detail="Task not found")

@app.patch("/tasks/{task_id}")
def patch_task(task_id: int, task: TaskPatch):
    for item in tasks:
        if item["id"] == task_id:
            if task.title is not None:
                item["title"] = task.title
            if task.completed is not None:
                item["completed"] = task.completed

            return item

    raise HTTPException(status_code=404, detail="Task not found")