from pydantic import BaseModel

class Post(BaseModel):
    id: int
    username: str
    content: str

class CreatePostBody(BaseModel):
    content: str

