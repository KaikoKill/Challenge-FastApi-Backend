from fastapi import FastAPI
from .middleware.mid import time_response
from .routers import users

app = FastAPI()
app.middleware("http")(time_response)

#rutas
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "API running"}