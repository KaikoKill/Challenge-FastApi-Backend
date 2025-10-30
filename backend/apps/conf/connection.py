from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from backend.apps.models.models import Base
from .settings import DATABASE_LOCAL_URL

engine = create_engine(DATABASE_LOCAL_URL)
SessionLocal = sessionmaker(bind=engine)

def get_db():
    try:
        instance = SessionLocal()
        yield instance
    finally:
        instance.close()

def init_db():
    Base.metadata.create_all(bind=engine)