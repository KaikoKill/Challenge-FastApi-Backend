from fastapi import APIRouter, FastAPI
from backend.apps.middleware.mid import time_response
from backend.apps.routers import users

app = FastAPI()
app.middleware("http")(time_response)

#rutas
app.include_router(users.router)