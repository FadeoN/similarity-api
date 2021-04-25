class FrameSimilarityDTO:
    def __init__(self,
                 score: float,
                 exerciseId: int,
                 exerciseName: str,
                 tag: str,
                 order: int):
        self.score = score
        self.exerciseId = exerciseId
        self.exerciseName = exerciseName
        self.tag = tag
        self.order = order
