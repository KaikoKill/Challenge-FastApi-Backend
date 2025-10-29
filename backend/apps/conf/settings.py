import os
from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from fastapi import FastAPI


app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(os.path.join(BASE_DIR,'.env'))
DATABASE_LOCAL_URL = os.path.join(BASE_DIR,"database","database.sqlite3") # tengo una carpeta para guardar la db

class Settings(BaseSettings):
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    DATABASE_URL: str = os.getenv("DATABASE_URL", DATABASE_LOCAL_URL)
    SECRET_KEY: str = os.getenv("SECRET_KEY", "todopython123")


settings = Settings()
