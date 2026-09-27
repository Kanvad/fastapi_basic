from fastapi import FastAPI
from app.routers.tasks import router

app = FastAPI()

app.include_router(router)

# GET request at the root URL.
# This is a simple health or welcome endpoint.
@app.get("/")
def root():
    return {"message": "Hello FastAPI"}

