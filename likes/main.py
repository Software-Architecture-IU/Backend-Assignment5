import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from likes.controller import router

app = FastAPI()

origins = ["*"]

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=False,
                   allow_methods=["*"],
                   allow_headers=["*"], )

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
