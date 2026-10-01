from fastapi import APIRouter, HTTPException, status, Depends

from app.schemas import OwnerCreate, OwnerResponse, OwnerUpdate, OwnerPatch
from app.data import owners, tasks
from app.dependencies import find_owner
from app.exceptions import OwnerInUseError

router = APIRouter(prefix="/owners", tags=["Owners"])


@router.get("", response_model=list[OwnerResponse])
def get_owners():
    return owners


@router.get("/{owner_id}", response_model=OwnerResponse)
def get_owner(owner: dict = Depends(find_owner)):
    return owner


@router.post("", response_model=OwnerResponse, status_code=status.HTTP_201_CREATED)
def create_owner(owner: OwnerCreate):
    new_owner = {
        "id": max((item["id"] for item in owners), default=0) + 1,
        "name": owner.name,
    }
    owners.append(new_owner)
    return new_owner


@router.delete("/{owner_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_owner(owner: dict = Depends(find_owner)):
    owner_is_used = any(
        task.get("owner_id") == owner["id"]
        for task in tasks
    )

    if owner_is_used:
        raise OwnerInUseError(owner["id"])

    owners.remove(owner)


@router.put("/{owner_id}", response_model=OwnerResponse)
def update_owner(owner_update: OwnerUpdate, owner: dict = Depends(find_owner)):
    owner["name"] = owner_update.name
    return owner


@router.patch("/{owner_id}", response_model=OwnerResponse)
def patch_owner(owner_patch: OwnerPatch, owner: dict = Depends(find_owner)):
    owner["name"] = (
        owner_patch.name if owner_patch.name is not None else owner["name"]
    )

    return owner