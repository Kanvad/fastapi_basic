from fastapi import Depends, HTTPException, status

from app.exceptions import TaskNotFoundError, OwnerNotFoundError
from app.services.owner_service import get_owner
from app.services.task_service import (
    get_task as get_task_service,
    get_task_owner as get_task_owner_service,
)


def find_task(task_id: int):
    task = get_task_service(task_id)
    if task is not None:
        return task

    raise TaskNotFoundError(task_id)


def find_owner(owner_id: int):
    return get_owner(owner_id)

def validate_owner_id(owner_id: int | None = None):
    if owner_id is None:
        return None

    return find_owner(owner_id)


def log_request():
    print("Request started")
    yield
    print("Request finished")



def get_task_owner(task: dict = Depends(find_task)):
    return get_task_owner_service(task)


def get_db():
    print("DB connection opened")

    db = {"connected": True}

    yield db

    print("DB connection closed")

def get_current_user():
    return {"id": 1, "name": "Phat"}