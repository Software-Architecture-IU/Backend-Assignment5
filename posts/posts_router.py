from typing import Annotated

from fastapi import APIRouter

router = APIRouter(prefix="/posts")


@router.get("/")
def get_posts():
    pass


@router.post("/")
def get_room():
    pass
