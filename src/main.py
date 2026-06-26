from fastapi import FastAPI

from src.api.routes import router as api_router

app = FastAPI(title="Proyecto Base")

app.include_router(api_router)

@app.get("/health")
def health():
    return {"status": "ok"}
