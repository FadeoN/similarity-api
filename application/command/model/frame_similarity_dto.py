from typing import List

from pydantic import BaseModel


class FrameSimilarityDTO(BaseModel):
    score: float
    exerciseId: int
    exerciseName: str
    tag: str
    order: int


class FrameSimilarityResponse(BaseModel):
    frameSimilarities: List[FrameSimilarityDTO]


