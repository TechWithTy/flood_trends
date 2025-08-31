import os


FEMA_API_BASE_URL = os.getenv("FEMA_API_BASE_URL", "https://www.fema.gov/api/open").rstrip("/")
FEMA_API_TIMEOUT = float(os.getenv("FEMA_API_TIMEOUT", "15"))