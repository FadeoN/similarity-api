from typing import Optional, List

from pydantic.main import BaseModel

from application.command.index_exercise_video_command import FrameVectorPair


class IndexExerciseVideoRequest(BaseModel):
    exerciseId: int
    exerciseName: str
    url: str
    tag: str
    frameVectorPairs: List[FrameVectorPair]
    index: Optional[str] = None
