from pydantic import BaseModel

class PredictionResponse(BaseModel):
    survival_prediction: int