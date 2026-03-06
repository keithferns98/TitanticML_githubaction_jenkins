from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from src.core.security import *
from src.logger.custom_logger import *

router =APIRouter()
logger =get_logger(__name__)

user_db = {
    "admin":{
        "username": "keith",
        "hashed_password": hash_password("ferns123")
    }
}
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = user_db.get("admin").get("hashed_password")
    if not user or not verify_password(form_data.password, user):
        logger.warning("Invalid login attempt")
        raise HTTPException(status_code =401, detail = "Invalid")

    access_token = create_access_token({"sub": form_data.username})
    refresh_token = create_refresh_token({"sub": form_data.username})

    logger.info("User logged in successfully")

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

@router.post("/refresh")
def refresh_token(refresh_token: str):
    payload = verify_token(refresh_token)

    if payload is None:
        raise HTTPException(status_code= 401, detail = "Invalid refresh token.")
    
    new_access_token = create_access_token({"sub": payload["sub"]})
    return {
        "access_token": new_access_token,
        "token_type": "bearer"
    }