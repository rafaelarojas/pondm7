from fastapi import FastAPI
from routers import crypto
from utils.logs import setup_logger
from db.db import Base, engine
from models import models

app = FastAPI()

logger = setup_logger()

@app.on_event("startup")
async def startup_event():
    logger.info("Sistema de Previsão de Criptomoedas Iniciado")
    
    models.Base.metadata.create_all(bind=engine)

app.include_router(crypto.router)
