from app.data import owners, tasks
from app.exceptions import OwnerInUseError, OwnerNotFoundError

def get_owners():
    return owners

def delete_owner(owner: dict):
    owner_is_used = any(
        task.get("owner_id") == owner["id"]
        for task in tasks
    )

    if owner_is_used:
        raise OwnerInUseError(owner["id"])

    owners.remove(owner)

def create_owner(name: str):
    new_owner = {
        "id": max((item["id"] for item in owners), default=0) + 1,
        "name": name,
    }
    owners.append(new_owner)
    return new_owner

def get_owner(owner_id: int):
    for owner in owners:
        if owner["id"] == owner_id:
            return owner
    raise OwnerNotFoundError(owner_id)

def update_owner(owner: dict, name: str):
    owner["name"] = name
    return owner

def patch_owner(owner: dict, name: str | None = None):
    owner["name"] = name if name is not None else owner["name"]
    return owner