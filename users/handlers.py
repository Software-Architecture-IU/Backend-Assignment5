import re

from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, Response

# User model
class User(BaseModel):
    username: str

# All the created user
users = set()

# Error messages & codes
invalid_username_code = 400
username_exists_code = 400
user_does_not_exist_code = 400

invalid_username_msg = "ERR_INVALID_USERNAME"
username_exists_msg = "ERR_USER_EXISTS"
user_does_not_exist_msg = "ERR_NO_USER"

router = APIRouter()

# Register new user
@router.post("/register", response_model=User)
def register(user: User):
    if user.username in users:
        raise HTTPException(username_exists_code, detail=username_exists_msg) 
    if not bool(re.match(r'^\w+$', user.username)):
        raise HTTPException(invalid_username_code, detail=invalid_username_msg)
    users.add(user.username)
    return user

# Check user existence
@router.post("/auth", response_model=User)
def auth(user: User):
    if user.username not in users:
        raise HTTPException(user_does_not_exist_code, 
                            detail=user_does_not_exist_msg) 
    return Response(status_code=200)
