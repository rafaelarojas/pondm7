from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import crypto  # Import do roteador de crypto
from utils.logs import setup_logger
import logging

app = FastAPI()

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuração do logger
logger = setup_logger()

# Evento de inicialização
@app.on_event("startup")
async def startup_event():
    logger.info("Sistema de Previsão de Criptomoedas Iniciado")

# Incluindo as rotas do módulo crypto
app.include_router(crypto.router)
