from fastapi import FastAPI
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

