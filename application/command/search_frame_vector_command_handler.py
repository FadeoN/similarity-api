from application.command.model.frame_similarity_dto import FrameSimilarityDTO, FrameSimilarityResponse
from application.command.search_frame_vector_command import SearchFrameVectorCommand
from infrastructure.config.elasticsearch import asyncElasticClient, frame_index_alias


async def handle(command: SearchFrameVectorCommand) -> FrameSimilarityResponse:
    query = {
        "_source": True,
        "size": command.size,
        "fields": ["exerciseId", "exerciseName", "tag", "order"],
        "query": {
            "knn": {
                "frameVector": {
                    "vector": command.vector,
                    "k": command.k
                }
            }
        },
    }

    resp = await asyncElasticClient.search(request_timeout=10,
                                           index=command.index,
                                           body=query)
    result = []
    for hit in resp["hits"]["hits"]:
        data = hit["_source"]

        result.append(FrameSimilarityDTO(score=hit["_score"],
                                         exerciseId=data["exerciseId"],
                                         exerciseName=data["exerciseName"],
                                         tag=data["tag"],
                                         order=data["order"]))
    return FrameSimilarityResponse(frameSimilarities=result)
