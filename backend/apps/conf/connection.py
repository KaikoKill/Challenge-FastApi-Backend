from sqlalchemy import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .settings import DATABASE_LOCAL_URL

Base = declarative_base()
engine = create_engine(DATABASE_LOCAL_URL)

SessionLocal = sessionmaker(bind=engine)