from typing import Optional

from pydantic import Field
from pydantic.main import BaseModel


class CreateFramesIndexRequest(BaseModel):
    indexName: Optional[str]
    shardCount: int = Field(default=1, ge=1, description="Shard count must be more than zero")
    replicaCount: int = Field(default=0, ge=0, description="Shard count must be more greater than or equal to zero")
    refreshIntervalSecond: int = Field(default=15, ge=1,
                                       description="Refresh interval must be greater than zero (in seconds)")
