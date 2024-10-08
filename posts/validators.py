from typing import Optional
from fastapi import HTTPException
import requests

from posts.database import posts

# Dependency to validate offset
def validate_offset(offset: Optional[int]=None) -> int:
    total_posts: int = len(posts)
    if offset is None:
        # Default offset: last 10 posts
        offset = total_posts - 10 if total_posts >= 10 else 0
    elif offset < 0 or offset > total_posts:
        raise HTTPException(status_code=400, detail="ERR_INVALID_OFFSET")

    return max(offset, 0)


def check_user_auth(username: str) -> str:
    body = {'username': username}
    url = "http://127.0.0.1:8999/auth"
    response = requests.post(url, json=body)
    if response.status_code == 200:
        return username
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)
