import hashlib

from application.command.delete_frame_index_command import DeleteFrameIndexCommand
from infrastructure.config.elasticsearch import frame_index_alias, asyncElasticClient


async def handle(command: DeleteFrameIndexCommand):
    if command.index is None:
        command.index = frame_index_alias

    await asyncElasticClient.delete(
        index=command.index,
        id=hashlib.md5(f"{command.exerciseId}_{command.order}".encode("utf-8")).hexdigest()
    )
