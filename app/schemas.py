from typing import Optional
from pydantic import BaseModel, Field


class OwnerCreate(BaseModel):
    id: int
    name: str

class OwnerResponse(BaseModel):
    id: int
    name: str

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    owner: Optional[OwnerCreate] = None


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
    owner: Optional[OwnerResponse] = None