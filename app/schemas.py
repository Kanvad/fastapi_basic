from typing import Optional
from pydantic import BaseModel, Field

class OwnerBase(BaseModel):
    name: str

class OwnerCreate(OwnerBase):
    pass

class OwnerResponse(OwnerBase):
    id: int

class OwnerUpdate(OwnerBase):
    pass

class OwnerPatch(BaseModel):
    name: Optional[str] = None

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    owner_id: Optional[int] = None


class TaskUpdate(BaseModel):
    title: str
    completed: bool

class TaskPatch(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    completed: Optional[bool] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool
    owner_id: Optional[int] = None