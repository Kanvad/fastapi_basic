from typing import Optional
from fastapi import APIRouter, status, Depends

from app.schemas import TaskCreate, TaskUpdate, TaskPatch, TaskResponse
from app.data import tasks
from app.dependencies import find_task, validate_owner_id, get_task_owner
from app.services.task_service import create_task as create_task_service, update_task as update_task_service, patch_task as patch_task_service, delete_task as delete_task_service



router = APIRouter(prefix="/tasks", tags=["Tasks"])




# GET /tasks
@router.get("", response_model=list[TaskResponse])
def get_tasks(owner: dict | None = Depends(validate_owner_id)):
    if owner is None:
        return tasks

    return [
        task
        for task in tasks
        if task.get("owner_id") == owner["id"]
    ]




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

@router.get("/{task_id}/owner", response_model=Optional[dict])
def get_task_owner_endpoint(owner: Optional[dict] = Depends(get_task_owner)):
    return owner


# POST /tasks
@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, owner: dict | None = Depends(validate_owner_id)):
    return create_task_service(task.title, task.owner_id)


# PUT /tasks/{task_id}
@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_update: TaskUpdate, task: dict = Depends(find_task)):
    return update_task_service(task, task_update.title, task_update.completed)



# DELETE /tasks/{task_id}
@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task: dict = Depends(find_task)):
    delete_task_service(task)


# PATCH /tasks/{task_id}
@router.patch("/{task_id}", response_model=TaskResponse)
def patch_task(task_patch: TaskPatch, task: dict = Depends(find_task)):
    return patch_task_service(
        task,
        title=task_patch.title,
        completed=task_patch.completed,
    )