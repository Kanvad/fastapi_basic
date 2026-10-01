from typing import Optional
from fastapi import APIRouter, HTTPException, status, Depends

from app.schemas import TaskCreate, TaskUpdate, TaskPatch, TaskResponse
from app.data import tasks
from app.dependencies import find_owner, find_task, validate_owner_id, log_request, get_task_owner, get_db, get_current_user
from app.services.task_service import create_task as create_task_service, update_task as update_task_service, patch_task as patch_task_service, delete_task as delete_task_service

API_KEY = "secret123"

def verify_api_key(api_key: str):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )

def get_current_api_key(api_key: str):
    return api_key

router = APIRouter(prefix="/tasks", tags=["Tasks"], dependencies=[Depends(log_request)])


@router.get("/some_endpoint")
def some_endpoint(api_key: str = Depends(get_current_api_key)):
    return {"api_key": api_key}

# GET /tasks
@router.get("", response_model=list[TaskResponse])
def get_tasks(
    owner: dict | None = Depends(validate_owner_id),_: None = Depends(log_request)
):
    if owner is None:
        return tasks

    return [
        task
        for task in tasks
        if task.get("owner_id") == owner["id"]
    ]

@router.get("/db")
def get_resource(db: str = Depends(get_db)):
    raise HTTPException(status_code=500, detail="Database error")

@router.get("/context")
def get_context(user: dict = Depends(get_current_user), db: dict = Depends(get_db)):
    return {"user": user, "db": db}

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
def create_task(task: TaskCreate):

    if task.owner_id is not None:
        find_owner(task.owner_id)

    return create_task_service(task.title, task.owner_id)


# PUT /tasks/{task_id}
@router.put("/{task_id}")
def update_task(task_update: TaskUpdate, task: dict = Depends(find_task)):
    return update_task_service(task, task_update.title, task_update.completed)



# DELETE /tasks/{task_id}
@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task: dict = Depends(find_task)):
    delete_task_service(task)


# PATCH /tasks/{task_id}
@router.patch("/{task_id}")
def patch_task(task_patch: TaskPatch, task: dict = Depends(find_task)):
    return patch_task_service(
        task,
        title=task_patch.title,
        completed=task_patch.completed,
    )