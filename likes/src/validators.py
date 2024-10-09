import requests
from fastapi import HTTPException


def is_auth(username: str):
    body = {'username': username}
    url = "http://stress-testers.ru:8999/auth"
    response = requests.post(url, json=body)
    if response.status_code == 200:
        return username
    else:
        return HTTPException(status_code=response.status_code, detail=response.text)
