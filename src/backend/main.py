from fastapi import FastAPI
from routers import crypto
from utils.logs import setup_logger  # Ajuste a importação para corresponder ao nome correto
import logging

app = FastAPI()

# Setup do Logger
logger = setup_logger()  # Chame a função correta para configurar o logger

@app.on_event("startup")
async def startup_event():
    logger.info("Sistema de Previsão de Criptomoedas Iniciado")

# Incluir as rotas de previsão
app.include_router(crypto.router)
