from typing import Optional
from fastapi import APIRouter, HTTPException, status, Depends

from app.schemas import OwnerCreate, OwnerResponse
from app.data import owners, tasks

router = APIRouter(prefix="/owners", tags=["Owners"])


def find_owner(owner_id: int):
    for owner in owners:
        if owner["id"] == owner_id:
            return owner

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Owner not found",
    )


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
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Owner is being used by a task",
        )

    owners.remove(owner)