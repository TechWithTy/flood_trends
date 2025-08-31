import os
from typing import Any, Dict, Optional

import requests
from app.core.third_party_integrations.flood_trends import config


class OpenFEMAClient:
    """
    Client for FEMA OpenFEMA datasets (Flood Trends use case).
    Docs: https://www.fema.gov/about/openfema/api

    Base: https://www.fema.gov/api/open/v1/{Dataset}

    Common datasets:
      - DisasterDeclarationsSummaries
      - Disasters
      - FimaNfipClaims
      - FimaNfipPolicies
    """

    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None, timeout: Optional[int] = None):
        # OpenFEMA doesn't require an API key for many datasets, but supports it via X-API-KEY
        self.api_key = api_key or os.getenv("OPENFEMA_API_KEY")
        resolved_base = base_url or os.getenv("OPENFEMA_BASE_URL") or getattr(config, "FEMA_API_BASE_URL", "https://www.fema.gov/api/open")
        # Ensure we use the v1 segment if caller passed base without it
        if not resolved_base.rstrip("/").endswith("/v1"):
            resolved_base = f"{resolved_base.rstrip('/')}/v1"
        self.base_url = resolved_base.rstrip("/")
        self.timeout = int(timeout if timeout is not None else getattr(config, "FEMA_API_TIMEOUT", 15))

    def _headers(self) -> Dict[str, str]:
        headers: Dict[str, str] = {"Accept": "application/json"}
        if self.api_key:
            headers["X-API-KEY"] = self.api_key
        return headers

    def query(self, dataset: str, *, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Generic query against a specific OpenFEMA dataset.

        Params can include $filter, $orderby, $select, $skip, $top, etc.
        Returns parsed JSON.
        """
        url = f"{self.base_url}/{dataset}"
        resp = requests.get(url, headers=self._headers(), params=params or {}, timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()

    def list_disaster_declarations(
        self,
        *,
        filter: Optional[str] = None,
        top: int = 1000,
        skip: int = 0,
        select: Optional[str] = None,
        orderby: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        GET https://www.fema.gov/api/open/v1/DisasterDeclarationsSummaries
        """
        params: Dict[str, Any] = {"$top": top, "$skip": skip}
        if filter:
            params["$filter"] = filter
        if select:
            params["$select"] = select
        if orderby:
            params["$orderby"] = orderby
        return self.query("DisasterDeclarationsSummaries", params=params)

    def list_disasters(
        self,
        *,
        filter: Optional[str] = None,
        top: int = 1000,
        skip: int = 0,
        select: Optional[str] = None,
        orderby: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        GET https://www.fema.gov/api/open/v1/Disasters
        """
        params: Dict[str, Any] = {"$top": top, "$skip": skip}
        if filter:
            params["$filter"] = filter
        if select:
            params["$select"] = select
        if orderby:
            params["$orderby"] = orderby
        return self.query("Disasters", params=params)