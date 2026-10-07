from app.data import tasks
from app.services.owner_service import get_owner
from app.repositories import task_repository

def get_task(task_id: int):
    return task_repository.get_by_id(task_id)

def get_tasks():
    return task_repository.get_all()

def get_completed_tasks():
    return task_repository.get_completed()

def get_task_owner(task: dict):
    owner_id = task.get("owner_id")
    if owner_id is not None:
        return get_owner(owner_id)
    return None

def create_task(title: str, owner_id: int | None = None):
    new_task = {
        "title": title,
        "completed": False,
        "owner_id": owner_id,
    }
    return task_repository.create(new_task)

def update_task(task: dict, title: str, completed: bool):
    return task_repository.update(task, title, completed)

def patch_task(
    task: dict,
    title: str | None = None,
    completed: bool | None = None,
):
    return task_repository.patch(task, title, completed)

def delete_task(task: dict):
    return task_repository.delete(task)