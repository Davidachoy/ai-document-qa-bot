from fastapi import APIRouter

router = APIRouter()


@router.post("/test")
async def test_endpoint(data: dict):
    return {
        "message": "Connection successful!",
        "received": data,
        "timestamp": "...",
    }
