from typing import List, Optional

from pydantic import Field
from pydantic.main import BaseModel


class SearchFrameVectorRequest(BaseModel):
    vector: List[float]
    k: Optional[int] = Field(default=5, ge=1, description="K must be more than zero")
    size: Optional[int] = Field(default=10, ge=1, description="Size must be more than zero")
