from fastapi import FastAPI
from users.handlers import router
from starlette.middleware.cors import CORSMiddleware

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


app.include_router(router)
