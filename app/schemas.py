from typing import Optional
from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    owner: Optional[Owner] = None


class TaskUpdate(BaseModel):
    title: str
    completed: bool

class TaskPatch(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    completed: Optional[bool] = None

class Owner(BaseModel):
    id: int
    name: str

class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool
    owner: Optional[Owner] = None