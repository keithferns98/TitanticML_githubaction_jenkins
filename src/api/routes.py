from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from src.core.security import verify_token
from src.schemas.request_schema import TitanicRequest
from fastapi import APIRouter
from src.logger.custom_logger import get_logger
from src.services.model_service import predict
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
# from src.preprocessing.preprocess import transform_input


router = APIRouter()
logger = get_logger(__name__)
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl= "/auth/login")

# def get_current_user(token: str = Depends(oauth2_scheme)):
#     payload = verify_token(token)
#     if payload is None:
#         raise HTTPException(status_code= 401, detail = "Invalid token")
#     return payload["sub"]

security = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials
    payload = verify_token(token)

    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    return payload["sub"]

@router.post("/predict")
def predict_survival(request: TitanicRequest,
                     current_user: str = Depends(get_current_user)):
    model_input = request.to_model_input()

    logger.info(
        f"User={current_user} | Input={model_input}"
    )
    model_input.pop("Name", None)
    result = predict(model_input)

    logger.info(
        f"User={current_user} | Prediction={result}")
    return {"survival_prediction": result}
