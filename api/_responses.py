from typing import Any, Dict, List, TypedDict


class OpenFEMAResult(TypedDict, total=False):
    # OpenFEMA returns arbitrary fields depending on dataset; keep it generic
    # Example common fields
    disasterNumber: int
    state: str
    declarationDate: str
    incidentType: str
    title: str


class OpenFEMAResponse(TypedDict):
    metadata: Dict[str, Any]
    results: List[OpenFEMAResult]