from typing import Optional

from pydantic.main import BaseModel


class DeleteFrameIndexRequest(BaseModel):
    exerciseId: int
    order: int
    index: Optional[str]
