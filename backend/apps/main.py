from fastapi import FastAPI
from backend.apps.middleware.mid import time_response

app = FastAPI()
app.add_middleware(time_response)
