import json
import random
import asyncio
from fastapi import APIRouter, Request
from sse_starlette.sse import EventSourceResponse

router = APIRouter()


async def generator(request: Request):
    value = None

    while not (await request.is_disconnected()):
        value_test = random.randint(0, 9)

        value = value_test in [3, 4, 5]

        if value != value_test:
            yield {
                "id": "test",
                "event": "emergency",
                "data": json.dumps({
                    "emergency": value
                }),
                "retry": 5000
                }

        await asyncio.sleep(1)


@router.get("/sse")
async def sse(request: Request):
    return EventSourceResponse(
        generator(request),
        ping=5
        )
