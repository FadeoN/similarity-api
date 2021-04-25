from typing import Optional

from pydantic.main import BaseModel


class IndexExerciseVideoRequest(BaseModel):
    exerciseId: int
    exerciseName: str
    url: str
    tag: str
    index: Optional[str] = None
