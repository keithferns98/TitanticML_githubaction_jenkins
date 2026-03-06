from fastapi import FastAPI
import uvicorn

from src.api import routes, auth
from src.exceptions.custom_exception import ModelException, model_exception_handler
from src.logger.custom_logger import get_logger

logger = get_logger(__name__)

app = FastAPI(
    title="Titanic Survival Prediction API",
    description="XGBoost-based ML API with Authentication",
    version="1.0.0"
)

# 🔹 Routers
app.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"]
)

app.include_router(
    routes.router,
    prefix="/model",
    tags=["Prediction"]
)

app.add_exception_handler(ModelException, model_exception_handler)


@app.get("/")
def root():
    return {"message": "Titanic Survival Prediction API is running 🚢"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.on_event("startup")
def startup_event():
    logger.info("Application started successfully")


@app.on_event("shutdown")
def shutdown_event():
    logger.info("Application shutdown")


# 🔥 Uvicorn Runner
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )