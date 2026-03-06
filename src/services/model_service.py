import joblib
import os
import pandas as pd
# from src.preprocessing.preprocess import transform_input

MODEL_PATH = os.path.join("artifacts", "xgb_model.pkl")
PREPROCESSOR_PATH = os.path.join("artifacts", "preprocessor.pkl")

model = joblib.load(MODEL_PATH)
preprocessor = joblib.load(PREPROCESSOR_PATH)

def predict(data: dict):
    df = pd.DataFrame([data])
    X_processed = preprocessor.transform(df)
    prediction = model.predict(X_processed)[0]
    return int(prediction)