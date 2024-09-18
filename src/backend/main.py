from fastapi import FastAPI
from routers import crypto
from utils.logs import setup_logger
import logging

app = FastAPI()

logger = setup_logger()

@app.on_event("startup")
async def startup_event():
    logger.info("Sistema de Previsão de Criptomoedas Iniciado")

app.include_router(crypto.router)
