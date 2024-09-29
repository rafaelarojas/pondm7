from fastapi import APIRouter, HTTPException
from models.model_loader import load_model
from models.train_models import retrain_models
from datetime import datetime
from utils.logs import setup_logger
from db.db import save_log, SessionLocal
from db.db import Log

logger = setup_logger()

router = APIRouter()

@router.get("/ml_models/{model_name}")
async def get_model(model_name: str):
    try:
        model = load_model(model_name)
        logger.info(f"Modelo {model_name} carregado")
        save_log(f"Modelo {model_name} carregado")
        return {"message": f"Modelo {model_name} esta pronto para uso."}
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/retrain-models")
async def retrain():
    result = retrain_models()
    return {"message": result}

@router.get("/logs")
async def get_logs():
    session = SessionLocal()
    logs = session.query(Log).all()
    session.close()
    return [{"id": log.id, "message": log.message, "timestamp": log.timestamp} for log in logs]
