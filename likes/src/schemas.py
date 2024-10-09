from typing import List

from pydantic import BaseModel

from likes.src.types import Likes


class GetLikesRequest(BaseModel):
    post_ids: List[int]


class GetLikesResponse(BaseModel):
    items: List[Likes]


class PostLikeRequest(BaseModel):
    post_id: int
