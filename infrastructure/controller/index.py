from fastapi import APIRouter
from starlette import status

from application.command import index_exercise_video_command_handler, delete_frame_index_command_handler, \
    create_frames_index_command_handler
from application.command.create_frames_index_command import CreateFramesIndexCommand
from application.command.delete_frame_index_command import DeleteFrameIndexCommand
from application.command.index_exercise_video_command import IndexExerciseVideoCommand
from application.external.video_embedding_api import get_frame_vectors
from infrastructure.controller.requests.create_frames_index_request import CreateFramesIndexRequest
from infrastructure.controller.requests.delete_frame_index_request import DeleteFrameIndexRequest
from infrastructure.controller.requests.index_exercise_video_request import IndexExerciseVideoRequest

router = APIRouter()


@router.post("/exercise", status_code=status.HTTP_204_NO_CONTENT)
async def index_exercise_video(request: IndexExerciseVideoRequest):
    try:
        frame_vector_pairs = await get_frame_vectors(request.url)

        await index_exercise_video_command_handler.handle(IndexExerciseVideoCommand(
            exercise_id=request.exerciseId,
            exercise_name=request.exerciseName,
            tag=request.tag,
            frame_vector_pairs=frame_vector_pairs,
            index=request.index
        ))
        return
    except Exception as e:
        raise e


@router.delete("/frame", status_code=status.HTTP_204_NO_CONTENT)
async def delete_frame_index(request: DeleteFrameIndexRequest):
    try:

        await delete_frame_index_command_handler.handle(DeleteFrameIndexCommand(
            exerciseId=request.exerciseId,
            order=request.order,
            index=request.index
        ))
        return
    except Exception as e:
        raise e


@router.post("/create-frames-index", status_code=status.HTTP_204_NO_CONTENT)
async def create_frame_index(request: CreateFramesIndexRequest):
    try:

        await create_frames_index_command_handler.handle(CreateFramesIndexCommand(
            name=request.indexName,
            shard_count=request.shardCount,
            replica_count=request.replicaCount,
            refresh_interval_in_seconds=request.refreshIntervalSecond
        ))
        return
    except Exception as e:
        raise e
