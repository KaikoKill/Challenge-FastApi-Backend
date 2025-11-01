from datetime import timedelta
from typing import Annotated, Any
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
import jwt

from ..conf.settings import settings
from ..models.schemas import ListUsers, UserCreate, UserPublic
from ..conf.connection import SessionDep, TokenDep
from ..service.user_service import create_user, get_current_user_db, get_users, authenticate
from ..conf import security

router = APIRouter(prefix="/users",
                   tags=["users"])

@router.post("/", response_model= UserPublic )
async def create_user_endpoint(session_db : SessionDep, request_user: UserCreate) -> Any:
    try:
        user= create_user(session_db, request_user)
        return user
    except Exception as e:
        raise HTTPException(status_code= 500, detail= f"Ocurrio un error {str(e)}")

@router.get("/", response_model= ListUsers)
async def read_users(session_db: SessionDep, token: TokenDep):
    try :
        return get_users(session_db)
    except Exception as e:
        raise HTTPException(status_code= 500, detail = f"Ocurrio un error {str(e)}")

@router.post("/login")
async def login(session_db: SessionDep, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Any:
    try:
        user = authenticate(session_db, form_data.username, form_data.password)
        if user:
            access_token_expire = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
            return {
                    "access_token": security.create_access_token(sub= user.id,
                                                                expires_delta=access_token_expire),
                    "token_type": "bearer",
                    }
        raise HTTPException(status_code=400, detail="Usuario incorrecto")
    except Exception as e:
        raise HTTPException(status_code=500, detail= f"Error: {str(e)}")

@router.get("/me", response_model= UserPublic)
async def current_user(session_db: SessionDep, token: TokenDep):
    payload: dict = jwt.decode(token, settings.SECRET_KEY, algorithms=[security.ALGORITHM])
    sub : str = payload.get("sub")
    user = get_current_user_db(session_db, sub)
    return user