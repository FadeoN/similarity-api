from typing import List

from pydantic import BaseModel


class FrameSimilarityDTO(BaseModel):
    score: float
    exerciseId: str
    exerciseName: str
    tag: str
    order: int


class FrameSimilarityResponse(BaseModel):
    frameSimilarities: List[FrameSimilarityDTO]


