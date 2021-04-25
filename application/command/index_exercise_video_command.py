from typing import List


class FrameVectorPair:
    def __init__(self, order: int, vector: List[float]):
        self.order = order
        self.vector = vector


class IndexExerciseVideoCommand:
    def __init__(self,
                 exercise_id: int,
                 exercise_name: str,
                 tag: str,
                 frame_vector_pairs: List[FrameVectorPair],
                 index: str
                 ):
        self.exercise_id = exercise_id
        self.exercise_name = exercise_name
        self.tag = tag
        self.frame_vector_pairs = frame_vector_pairs
        self.index = index
