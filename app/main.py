from fastapi import FastAPI, status, HTTPException
from typing import Optional

from app.schemas import TaskCreate, TaskUpdate, TaskPatch, TaskResponse
from app.routers.tasks import router

app = FastAPI()

app.include_router(router)

# GET request at the root URL.
# This is a simple health or welcome endpoint.
@app.get("/")
def root():
    return {"message": "Hello FastAPI"}

