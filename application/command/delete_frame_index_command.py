class DeleteFrameIndexCommand:
    def __init__(self, exerciseId: str, order: int, index: str):
        self.exerciseId = exerciseId
        self.order = order
        self.index = index
