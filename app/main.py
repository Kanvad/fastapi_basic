from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions import TaskNotFoundError
from app.routers.tasks import router as tasks_router
from app.routers.owners import router as owners_router


app = FastAPI()

app.include_router(tasks_router)
app.include_router(owners_router)

# GET request at the root URL.
# This is a simple health or welcome endpoint.
@app.get("/")
def root():
    return {"message": "Hello FastAPI"}

@app.exception_handler(TaskNotFoundError)
async def task_not_found_exception_handler(
    request: Request,
    exc: TaskNotFoundError,
):
    return JSONResponse(
        status_code=404,
        content={"detail": f"Task {exc.task_id} not found"},
    )