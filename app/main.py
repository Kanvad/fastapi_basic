from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions import APIException, TaskNotFoundError
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

@app.exception_handler(APIException)
async def api_exception_handler(
    request: Request,
    exc: APIException,
):
    return JSONResponse(
        status_code=exc.status_code,
        content={"code": exc.code, "message": exc.detail},
    )