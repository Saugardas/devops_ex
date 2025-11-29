# app/ml/model.py
import pickle
import os
import numpy as np

MODEL_DIR = os.path.join(os.path.dirname(__file__), "../../models")
MODEL_PATH = os.path.join(MODEL_DIR, "best_model.pkl")
SCALER_PATH = os.path.join(MODEL_DIR, "scaler.pkl")
CLASS_NAMES_PATH = os.path.join(MODEL_DIR, "class_names.pkl")

# Глобальные переменные для модели, скалера и имён классов
_model = None
_scaler = None
_class_names = None

def load_artifacts():
    """Загружает модель, скалер и имена классов"""
    global _model, _scaler, _class_names
    with open(MODEL_PATH, 'rb') as f:
        _model = pickle.load(f)
    with open(SCALER_PATH, 'rb') as f:
        _scaler = pickle.load(f)
    with open(CLASS_NAMES_PATH, 'rb') as f:
        _class_names = pickle.load(f)

def predict(sepal_length: float, sepal_width: float) -> str:
    """Выполняет предсказание на основе входных признаков."""
    if _model is None or _scaler is None or _class_names is None:
        raise RuntimeError("Артефакты модели не загружены")
    
    # Подготовка данных - прогоняем через скалер
    features = np.array([[sepal_length, sepal_width]])
    features_scaled = _scaler.transform(features)
    
    # Предсказание с помощью нашей модели
    pred_index = _model.predict(features_scaled)[0]
    return _class_names[pred_index]
