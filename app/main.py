from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.database import Base, engine
from app.models.owner import Owner
from app.models.task import Task
from app.routers.tasks import router as tasks_router
from app.routers.owners import router as owners_router
from app.exceptions import APIException


Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(tasks_router)
app.include_router(owners_router)


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
        content={
            "error": {
                "code": exc.code,
                "message": exc.detail,
            }
        },
    )