from fastapi import APIRouter


router = APIRouter(prefix="/users",
                   tags=["users"])

@router.get("/")
async def users() -> dict:
    return {
        "message": "first endopoint"
    }