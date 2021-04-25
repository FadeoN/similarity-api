from typing import List


class SearchFrameVectorCommand:
    def __init__(self,
                 vector: List[float],
                 k: int = 10,
                 size: int = 5):
        self.vector = vector
        self.k = k
        self.size = size
