from fastapi import APIRouter
from app.ml.model import predict

router = APIRouter()

@router.get("/health")
async def health():
    return {"status": "ok"}

@router.get("/predict")
async def predict_handler(sepal_length: float, sepal_width: float):
    prediction = predict(sepal_length, sepal_width)
    return {"prediction": prediction}
