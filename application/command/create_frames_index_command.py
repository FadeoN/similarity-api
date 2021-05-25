from datetime import datetime
from typing import Optional

from application.utils import text_utils


class CreateFramesIndexCommand:
    def __init__(self,
                 name: Optional[str],
                 shard_count: int,
                 replica_count: int,
                 refresh_interval_in_seconds: int):
        if text_utils.is_blank(name):
            name = "frames_" + datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        self.name = name
        self.shard_count = shard_count
        self.replica_count = replica_count
        self.refresh_interval_in_seconds = refresh_interval_in_seconds
