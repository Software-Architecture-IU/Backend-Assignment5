import requests
from fastapi import APIRouter, Depends, HTTPException

import likes.src.schemas
import likes.src.validators as validators
from likes.src.database import likes
from likes.src.schemas import GetLikesResponse, GetLikesRequest, PostLikeRequest
from likes.src.types import Likes

router = APIRouter(prefix="")


@router.post("/likes")
async def get_likes(body: GetLikesRequest, username: str = Depends(validators.is_auth)) -> GetLikesResponse:
    if type(username) is not str:
        raise username

    existing = extract_existing(body, username)

    return GetLikesResponse(items=[extract_post_info(post_id) for post_id in existing])


@router.post("/like")
def post_like(body: PostLikeRequest, username: str = Depends(validators.is_auth)) -> str:
    if not is_exist(body.post_id, username):
        raise HTTPException(404, "ERR_NOT_FOUND")

    info = extract_post_info(body.post_id)
    if info is None:
        info = Likes(post_id=body.post_id, usernames=[])
        likes.append(info)

    if info.usernames.count(username) != 0:
        info.usernames.remove(username)
        return 'false'
    else:
        info.usernames.append(username)
        return 'true'


def extract_existing(ids: GetLikesRequest, username: str) -> [int]:
    return [post_id for post_id in ids.post_ids if is_exist(post_id, username)]


def is_exist(post_id: int, username: str) -> bool:
    url = f'http://stress-testers.ru:8043/posts/{post_id}?username={username}'
    return requests.get(url).status_code == 200


def extract_post_info(post_id: int):
    for entry in likes:
        if entry.post_id == post_id: return entry
    return None
