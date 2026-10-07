from fastapi import APIRouter, HTTPException, status

from app.data import tasks
from app.schemas import TaskCreate, TaskUpdate, TaskPatch, TaskResponse


router = APIRouter(prefix="/tasks", tags=["Tasks"])


def find_task(task_id: int) -> dict:
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task with ID {task_id} not found",
    )


# GET /tasks
@router.get("", response_model=list[TaskResponse])
def get_tasks():
    return tasks


# GET /tasks/{task_id}
@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    return find_task(task_id)


# POST /tasks
@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    new_task = {
        "id": max((item["id"] for item in tasks), default=0) + 1,
        "title": task.title,
        "completed": False,
    }
    tasks.append(new_task)
    return new_task


# PUT /tasks/{task_id}
@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskUpdate):
    task = find_task(task_id)
    task["title"] = task_update.title
    task["completed"] = task_update.completed
    return task


# PATCH /tasks/{task_id}
@router.patch("/{task_id}", response_model=TaskResponse)
def patch_task(task_id: int, task_patch: TaskPatch):
    task = find_task(task_id)
    if task_patch.title is not None:
        task["title"] = task_patch.title
    if task_patch.completed is not None:
        task["completed"] = task_patch.completed
    return task


# DELETE /tasks/{task_id}
@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    task = find_task(task_id)
    tasks.remove(task)