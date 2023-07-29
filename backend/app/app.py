from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from sse import router


app = FastAPI()
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
