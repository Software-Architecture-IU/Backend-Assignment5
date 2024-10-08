import fastapi

from starlette.middleware.cors import CORSMiddleware

from fastapi import FastAPI

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)



