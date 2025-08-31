from pydantic import BaseModel, Field
from typing import Optional


class DatasetQuery(BaseModel):
    filter: Optional[str] = Field(default=None, alias="$filter")
    top: int = Field(1000, ge=1, alias="$top")
    skip: int = Field(0, ge=0, alias="$skip")
    select: Optional[str] = Field(default=None, alias="$select")
    orderby: Optional[str] = Field(default=None, alias="$orderby")