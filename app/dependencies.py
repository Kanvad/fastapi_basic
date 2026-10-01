from fastapi import Depends, HTTPException, status

from app.data import owners, tasks
from app.exceptions import TaskNotFoundError, OwnerNotFoundError


def find_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise TaskNotFoundError(task_id)


def find_owner(owner_id: int):
    for owner in owners:
        if owner["id"] == owner_id:
            return owner

    raise OwnerNotFoundError(owner_id)

def validate_owner_id(owner_id: int | None = None):
    if owner_id is None:
        return None

    return find_owner(owner_id)


def log_request():
    print("Request started")
    yield
    print("Request finished")


def get_task_owner(task: dict = Depends(find_task)):
    owner_id = task.get("owner_id")
    if owner_id is not None:
        return find_owner(owner_id)
    return None

def get_db():
    print("DB connection opened")

    db = {"connected": True}

    yield db

    print("DB connection closed")

def get_current_user():
    return {"id": 1, "name": "Phat"}