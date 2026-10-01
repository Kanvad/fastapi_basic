from app.data import owners, tasks
from app.services.owner_service import get_owner

def get_tasks(owner: dict | None = None):
    if owner is None:
        return tasks

    return [
        task
        for task in tasks
        if task.get("owner_id") == owner["id"]
    ]

def get_completed_tasks():
    return [task for task in tasks if task["completed"]]

def get_task_owner(task: dict):
    owner_id = task.get("owner_id")
    if owner_id is not None:
        return get_owner(owner_id)
    return None

def create_task(title: str, owner_id: int | None = None):
    new_task = {
        "id": max((item["id"] for item in tasks), default=0) + 1,
        "title": title,
        "completed": False,
        "owner_id": owner_id,
    }
    tasks.append(new_task)
    return new_task

def update_task(task: dict, title: str, completed: bool):
    task["title"] = title
    task["completed"] = completed
    return task

def patch_task(
    task: dict,
    title: str | None = None,
    completed: bool | None = None,
):
    task["title"] = title if title is not None else task["title"]
    task["completed"] = completed if completed is not None else task["completed"]
    return task

def delete_task(task: dict):
    tasks.remove(task)