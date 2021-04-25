from typing import List

from application.command.index_exercise_video_command import FrameVectorPair

async def get_frame_vectors(url: str) -> List[FrameVectorPair]:
    raise NotImplementedError()
    # return [FrameVectorPair(order=i, vector=[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]) for i in range(10)]