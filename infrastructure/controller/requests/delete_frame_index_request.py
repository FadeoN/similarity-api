from typing import Optional

from pydantic.main import BaseModel


class DeleteFrameIndexRequest(BaseModel):
    exerciseId: str
    order: int
    index: Optional[str]
