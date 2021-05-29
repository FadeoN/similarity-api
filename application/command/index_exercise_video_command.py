from typing import List

from pydantic.main import BaseModel


class FrameVectorPair(BaseModel):
    order: int
    vector: List[float]



class IndexExerciseVideoCommand:
    def __init__(self,
                 exercise_id: int,
                 exercise_name: str,
                 tag: str,
                 url: str,
                 frame_vector_pairs: List[FrameVectorPair],
                 index: str
                 ):
        self.exercise_id = exercise_id
        self.exercise_name = exercise_name
        self.tag = tag
        self.url = url
        self.frame_vector_pairs = frame_vector_pairs
        self.index = index
