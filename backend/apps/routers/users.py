from datetime import timedelta
from typing import Annotated, Any
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
import jwt

from ..conf.settings import settings
from ..models.schemas import ListUsers, UserCreate, UserPublic, UserUpdate
from ..conf.connection import CurrentUserDep, SessionDep, current_user_dep
from ..service.user_service import create_user, delete_user, get_users, authenticate, update_user, get_user_by_id
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

@router.get("/", response_model= ListUsers, dependencies=[Depends(current_user_dep)])
async def read_users(session_db: SessionDep):
    try :
        return get_users(session_db)
    except:
        raise HTTPException(status_code= 401, detail = "No autorizado")
@router.patch("/update/{user_id}", response_model= UserPublic, dependencies=[Depends(current_user_dep)])
async def update_user_endpoint(session_db: SessionDep, user_id: int, user_update: UserUpdate) -> Any:
    try:
        user_db = get_user_by_id(session_db, user_id)
        updated_user = update_user(session_db, user_db, user_update)
        return updated_user
    except Exception as e:
        raise HTTPException(status_code= 500, detail= f"Ocurrio un error {str(e)}")

@router.patch("/delete/{user_id}", dependencies=[Depends(current_user_dep)])
async def delete_user_endpoint(session_db: SessionDep,  user_id: int):
    try:
        result = delete_user(session_db, user_id)
        return result
    except Exception as e:
        raise HTTPException(status_code= 500, detail= f"Ocurrio un error {str(e)}")

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
async def current_user(current_user: CurrentUserDep):
    return current_user