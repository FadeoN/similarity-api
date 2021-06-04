from application.command.create_frames_index_command import CreateFramesIndexCommand
from infrastructure.config.elasticsearch import asyncElasticClient


async def handle(command: CreateFramesIndexCommand) -> str:
    mapping = {
        "settings": {
            "index": {
                "knn": True,
                "knn.space_type": "cosinesimil",
                "knn.algo_param": {
                    "ef_search": 512,
                    "ef_construction": 512,
                    "m": 16
                },
                "number_of_shards": command.shard_count,
                "refresh_interval": f"{command.refresh_interval_in_seconds}s",
                "number_of_replicas": command.replica_count,
                "translog.flush_threshold_size": "2gb"
            }
        },
        "mappings": {
            "properties": {
                "frameVector": {
                    "type": "knn_vector",
                    "dimension": 16
                },
                "order": {
                    "type": "long"
                },
                "exerciseId": {
                    "type": "text",
                },
                "indexedAt": {
                    "type": "date"
                }
            }
        }
    }

    await asyncElasticClient.indices.create(index=command.name, body=mapping)
    return command.name
