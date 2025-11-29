from fastapi import FastAPI
from app.api import routes
from app.ml.model import load_artifacts

load_artifacts() # загрузка артефактов

app = FastAPI(title="Iris Classifier API")

app.include_router(routes.router)