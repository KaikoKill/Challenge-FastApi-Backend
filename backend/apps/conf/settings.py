import os
from pathlib import Path
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
APPS_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR,'.env'))

DB_FILE = os.path.join(APPS_DIR,"database","database.sqlite3") # tengo una carpeta para guardar la db
DATABASE_LOCAL_URL = f"sqlite:///{DB_FILE}"
class Settings(BaseSettings):
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    DATABASE_URL: str = os.getenv("DATABASE_URL", DATABASE_LOCAL_URL)
    SECRET_KEY: str = os.getenv("SECRET_KEY", "todopython123")


settings = Settings()
