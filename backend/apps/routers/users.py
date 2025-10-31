from typing import Any
from fastapi import APIRouter
from ..models.schemas import ListUsers, UserCreate, UserPublic
from ..conf.connection import SessionDep, TokenDep
from ..service.user_service import create_user, get_users


router = APIRouter(prefix="/users",
                   tags=["users"])
@router.post("/", response_model= UserPublic )
async def create_user_endpoint(session_db : SessionDep, request_user: UserCreate) ->Any:
    user= create_user(session_db, request_user)
    return user

@router.get("/", response_model= ListUsers)
async def read_users(session_db: SessionDep):
    return get_users(session_db)
