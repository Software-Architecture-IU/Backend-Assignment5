from dataclasses import dataclass
from typing import List


@dataclass
class Likes:
    post_id: int
    usernames: List[str]
