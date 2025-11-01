from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
import jwt
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine

from ..service.user_service import get_current_user_db

from ..models.models import Base, User
from .settings import DATABASE_LOCAL_URL
from .settings import settings
from .security import ALGORITHM
from collections.abc import Generator
from typing import Annotated


engine = create_engine(DATABASE_LOCAL_URL)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl = f"/users/login")

def get_db() -> Generator[Session, None, None]:
    instance = SessionLocal()
    try:
        yield instance
    finally:
         instance.close()

SessionDep= Annotated[Session, Depends(get_db)]
TokenDep = Annotated[str, Depends(reusable_oauth2)]

