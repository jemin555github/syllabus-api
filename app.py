from fastapi import FastAPI
from src.routes.router import router

app = FastAPI()
app.include_router(router)
