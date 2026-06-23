from fastapi import FastAPI
from src.api.v1.routes import router

app = FastAPI(title="Proyecto Base")

app.include_router(router)


@app.get("/")
def root():
    return {"status": "ok"}
