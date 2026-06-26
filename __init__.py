from fastapi import APIRouter

from .health import router as health_router
from .seme import router as seme_router
from .ventas import router as ventas_router

router = APIRouter()

router.include_router(health_router)
router.include_router(seme_router)
router.include_router(ventas_router)
