import hashlib
from datetime import datetime, timezone

from elasticsearch import helpers

from application.command.index_exercise_video_command import IndexExerciseVideoCommand
from infrastructure.config.elasticsearch import asyncElasticClient, frame_index_alias


async def handle(command: IndexExerciseVideoCommand):
    if command.index is None:
        command.index = frame_index_alias

    actions = [
        {
            "_index": command.index,
            "_source": {
                "frameVector": frame_vector_pair.vector,
                "exerciseId": command.exercise_id,
                "exerciseName": command.exercise_name,
                "tag": command.tag,
                "url": command.url,
                "order": frame_vector_pair.order,
                "indexedAt": datetime.now(timezone.utc),
            }
        } for frame_vector_pair in command.frame_vector_pairs
    ]

    await helpers.async_bulk(asyncElasticClient, actions=actions)
