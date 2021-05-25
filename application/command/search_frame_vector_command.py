from typing import List


class SearchFrameVectorCommand:
    def __init__(self,
                 vector: List[float],
                 index: str,
                 k: int = 10,
                 size: int = 5):
        self.vector = vector
        self.k = k
        self.size = size
        self.index = index
