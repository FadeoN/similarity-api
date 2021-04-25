from typing import List

from fastapi import APIRouter
from starlette import status

from application.command import search_frame_vector_command_handler
from application.command.model.frame_similarity_dto import FrameSimilarityDTO
from application.command.search_frame_vector_command import SearchFrameVectorCommand
from infrastructure.controller.requests.search_frame_vector_request import SearchFrameVectorRequest

router = APIRouter()


@router.post("/frame", status_code=status.HTTP_200_OK)
async def index_exercise_video(request: SearchFrameVectorRequest) -> List[FrameSimilarityDTO]:
    try:
        return await search_frame_vector_command_handler.handle(SearchFrameVectorCommand(
            vector=request.vector,
            k=request.k,
            size=request.size
        ))
    except Exception as e:
        raise e
