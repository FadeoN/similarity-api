from typing import List

from fastapi import APIRouter
from starlette import status

from application.command import search_frame_vector_command_handler
from application.command.model.frame_similarity_dto import FrameSimilarityResponse
from application.command.search_frame_vector_command import SearchFrameVectorCommand
from infrastructure.controller.requests.search_frame_vector_request import SearchFrameVectorRequest

router = APIRouter()


@router.post("/frame", status_code=status.HTTP_200_OK)
async def search_frame_similarity(request: SearchFrameVectorRequest) -> FrameSimilarityResponse:
    try:
        return await search_frame_vector_command_handler.handle(SearchFrameVectorCommand(
            vector=request.vector,
            k=request.k,
            size=request.size,
            index=request.index
        ))
    except Exception as e:
        raise e
