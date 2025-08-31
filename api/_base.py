import requests
from requests import Session

from app.core.third_party_integrations.flood_trends import config


class OpenFEMABase:
    """
    Lightweight base for OpenFEMA dataset requests.
    Uses FEMA_API_BASE_URL and FEMA_API_TIMEOUT from config.
    """

    def __init__(self):
        self.session: Session = requests.Session()
        self.base_url: str = getattr(config, "FEMA_API_BASE_URL", "https://www.fema.gov/api/open").rstrip("/")
        self.timeout: int = int(getattr(config, "FEMA_API_TIMEOUT", 15))

    def get(self, path: str, *, params: dict | None = None, headers: dict | None = None):
        url = f"{self.base_url}/{path.lstrip('/')}"
        resp = self.session.get(url, params=params or {}, headers=headers or {}, timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()