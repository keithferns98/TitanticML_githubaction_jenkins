import joblib
import os
import pandas as pd
# from src.preprocessing.preprocess import transform_input

MODEL_PATH = os.path.join("artifacts", "xgb_model.pkl")
PREPROCESSOR_PATH = os.path.join("artifacts", "preprocessor.pkl")

model = None
preprocessor = None

def load_model():
    global model
    if model is None:
        model = joblib.load(MODEL_PATH)
    return model

def load_preprocessor():
    global preprocessor
    if preprocessor is None:
        preprocessor = joblib.load(PREPROCESSOR_PATH)
    return preprocessor

def predict(data: dict):
    df = pd.DataFrame([data])
    model = load_model()
    preprocessor = load_preprocessor()
    X_processed = preprocessor.transform(df)
    prediction = model.predict(X_processed)[0]
    return int(prediction)