from fastapi import HTTPException, status

from app.data import owners, tasks


def find_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task not found",
    )


def find_owner(owner_id: int):
    for owner in owners:
        if owner["id"] == owner_id:
            return owner

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Owner not found",
    )


def validate_owner_id(owner_id: int | None = None):
    if owner_id is None:
        return None

    return find_owner(owner_id)

