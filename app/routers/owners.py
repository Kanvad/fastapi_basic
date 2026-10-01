from fastapi import APIRouter, HTTPException, status, Depends

from app.schemas import OwnerCreate, OwnerResponse, OwnerUpdate, OwnerPatch
from app.dependencies import find_owner
from app.exceptions import OwnerInUseError
from app.services.owner_service import (
    get_owners as get_owners_service,
    delete_owner as delete_owner_service,
    create_owner as create_owner_service,
    update_owner as update_owner_service,
    patch_owner as patch_owner_service
)

router = APIRouter(prefix="/owners", tags=["Owners"])


@router.get("", response_model=list[OwnerResponse])
def get_owners():
    return get_owners_service()


@router.get("/{owner_id}", response_model=OwnerResponse)
def get_owner(owner: dict = Depends(find_owner)):
    return owner


@router.post("", response_model=OwnerResponse, status_code=status.HTTP_201_CREATED)
def create_owner_endpoint(owner: OwnerCreate):
    return create_owner_service(owner.name)


@router.delete("/{owner_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_owner_endpoint(owner: dict = Depends(find_owner)):
    delete_owner_service(owner)


@router.put("/{owner_id}", response_model=OwnerResponse)
def update_owner(owner_update: OwnerUpdate, owner: dict = Depends(find_owner)):
    return update_owner_service(owner, owner_update.name)


@router.patch("/{owner_id}", response_model=OwnerResponse)
def patch_owner(owner_patch: OwnerPatch, owner: dict = Depends(find_owner)):
    return patch_owner_service(owner, owner_patch.name)