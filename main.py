from src.core.logging import configure_logging

configure_logging()

import logging

logger = logging.getLogger(__name__)

from fastapi import FastAPI
from seme.api.routes.health import router as health_router
from seme.api.routes.pipeline import router as pipeline_router

app = FastAPI()
logger.info("SEME Control Tower iniciando...")
app.include_router(health_router, prefix="/v1")
app.include_router(pipeline_router, prefix="/v1")
