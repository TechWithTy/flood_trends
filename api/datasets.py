import logging
from typing import Dict, Optional

from fastapi import APIRouter, Query

from app.core.third_party_integrations.flood_trends.client import OpenFEMAClient

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/openfema", tags=["flood_trends-datasets"])


# Utility

def query_dataset(dataset: str, *, filter: Optional[str], top: int, skip: int, select: Optional[str], orderby: Optional[str]) -> Dict:
    client = OpenFEMAClient()
    params: Dict[str, str] = {"$top": str(top), "$skip": str(skip)}
    if filter:
        params["$filter"] = filter
    if select:
        params["$select"] = select
    if orderby:
        params["$orderby"] = orderby
    return client.query(dataset, params=params)


# Routes
@router.get("/health")
async def health() -> Dict:
    client = OpenFEMAClient()
    return {
        "healthy": bool(client.base_url),
        "base_url": client.base_url,
        "has_api_key": bool(client.api_key),
    }

@router.get("/{dataset}")
async def openfema_dataset(dataset: str, filter: Optional[str] = Query(default=None), top: int = 1000, skip: int = 0, select: Optional[str] = None, orderby: Optional[str] = None) -> Dict:
    return query_dataset(dataset, filter=filter, top=top, skip=skip, select=select, orderby=orderby)

