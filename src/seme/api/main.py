# src/seme/api/main.py
from fastapi import FastAPI
from src.seme.api.v1.routes import router

app = FastAPI(title="SEME API")

app.include_router(router, prefix="/v1")
