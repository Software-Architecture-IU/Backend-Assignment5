from typing import Annotated, Optional
from fastapi import APIRouter, Depends, HTTPException

import posts.schemas as schemas
import posts.types as types
import posts.validators as validators
from posts.database import posts

router = APIRouter(prefix="/posts")

@router.get("/")
def get_posts_by_offset(username: str = Depends(validators.check_user_auth), offset=Depends(validators.validate_offset)) -> list[schemas.Post]:
    start_idx = max(offset, 0)
    end_idx = min(offset+10, len(posts))

    return [schemas.Post(id=id,
                         username=post.username,
                         content=post.content) for id, post in zip(range(start_idx, end_idx), posts[start_idx:end_idx])]


@router.post("/")
def create_post(body: schemas.CreatePostBody, username: str = Depends(validators.check_user_auth)) -> schemas.Post:
    post = types.Post(username=username, content=body.content)
    id_of_post = len(posts)
    posts.append(post)
    return schemas.Post(id=id_of_post, username=username, content=body.content)


@router.get("/{id}")
def get_post_by_id(id: int, username: str = Depends(validators.check_user_auth)) -> schemas.Post:
    if not (0 < id < len(posts)):
        return HTTPException(400, "ERR_ID_OUT_OF_RANGE")

    post = posts[id]
    return schemas.Post(id=id, username=username, content=post.content)
