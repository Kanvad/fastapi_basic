from fastapi import FastAPI

from app.routers.tasks import router as tasks_router


app = FastAPI(title="Task API")

app.include_router(tasks_router)


@app.get("/")
def root():
    return {"message": "Hello FastAPI"}