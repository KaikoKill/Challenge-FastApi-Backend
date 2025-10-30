from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from .settings import DATABASE_LOCAL_URL

Base = declarative_base()

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