from fastapi import FastAPI
from app.api import routes

app = FastAPI(title="Iris Classifier API")

app.include_router(routes.router)