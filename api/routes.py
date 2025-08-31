import logging
from typing import Dict, Optional

from fastapi import APIRouter
from app.core.third_party_integrations.flood_trends.api.datasets import router as datasets_router
from app.core.third_party_integrations.flood_trends.api.disasters import router as disasters_router
from app.core.third_party_integrations.flood_trends.api.declarations import router as declarations_router

logger = logging.getLogger(__name__)
router = APIRouter()

# Aggregate sub-routers
router.include_router(datasets_router)
router.include_router(disasters_router)
router.include_router(declarations_router)

