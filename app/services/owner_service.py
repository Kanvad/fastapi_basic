from app.data import tasks
from app.exceptions import OwnerInUseError, OwnerNotFoundError
from app.repositories import owner_repository

def get_owners():
    return owner_repository.get_all()

def delete_owner(owner: dict):
    owner_is_used = any(
        task.get("owner_id") == owner["id"]
        for task in tasks
    )

    if owner_is_used:
        raise OwnerInUseError(owner["id"])

    return owner_repository.delete(owner)

def create_owner(name: str):
    return owner_repository.create({"name": name})

def get_owner(owner_id: int):
    owner = owner_repository.get_by_id(owner_id)
    if owner is None:
        raise OwnerNotFoundError(owner_id)
    return owner

def update_owner(owner: dict, name: str):
    return owner_repository.update(owner, name)

def patch_owner(owner: dict, name: str | None = None):
    return owner_repository.patch(owner, name)