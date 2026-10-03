from app.data import owners

def get_by_id(owner_id: int):
    for owner in owners:
        if owner["id"] == owner_id:
            return owner
    return None

def create(owner: dict):
    owner["id"] = max(
        (item["id"] for item in owners),
        default=0,
    ) + 1

    owners.append(owner)

    return owner

def delete(owner: dict):
    owners.remove(owner)

def update(owner: dict, name: str):
    owner["name"] = name
    return owner

def patch(owner: dict, name: str | None = None):
    owner["name"] = name if name is not None else owner["name"]
    return owner

def get_all():
    return owners