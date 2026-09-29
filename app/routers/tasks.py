from typing import Optional
from fastapi import APIRouter, HTTPException, status, Depends

from app.schemas import TaskCreate, TaskUpdate, TaskPatch, TaskResponse
from app.data import tasks

router = APIRouter(prefix="/tasks", tags=["Tasks"])

def find_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found",
    )

# GET /tasks?completed=true
@router.get("", response_model=list[TaskResponse])
def get_tasks(completed: Optional[bool] = None):

    if completed is None:
        return tasks

    filtered_tasks = []

    for task in tasks:
        if task["completed"] == completed:
            filtered_tasks.append(task)

    return filtered_tasks

# GET /tasks/completed
@router.get("/completed", response_model=list[TaskResponse])
def get_completed_tasks():
    completed_tasks = []
    for task in tasks:
        if task["completed"]:
            completed_tasks.append(task)
    return completed_tasks


# GET /tasks/{task_id}
@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task: dict = Depends(find_task)):
    return task



# POST /tasks
@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "completed": False
    }

    tasks.append(new_task)

    return new_task


# PUT /tasks/{task_id}
@router.put("/{task_id}")
def update_task(task_update: TaskUpdate, task: dict = Depends(find_task)):
    if task_update is not None:
        task["title"] = task_update.title
        task["completed"] = task_update.completed

    return task



# DELETE /tasks/{task_id}
@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task: dict = Depends(find_task)):
    tasks.remove(task)


# PATCH /tasks/{task_id}
@router.patch("/{task_id}")
def patch_task(task_patch: TaskPatch, task: dict = Depends(find_task)):
    if task_patch.title is not None:
        task["title"] = task_patch.title
    if task_patch.completed is not None:
        task["completed"] = task_patch.completed

    return task