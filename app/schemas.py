from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)


class TaskUpdate(BaseModel):
    title: str
    completed: bool


class TaskPatch(BaseModel):
    title: str | None = Field(None, min_length=3, max_length=100)
    completed: bool | None = None


class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool