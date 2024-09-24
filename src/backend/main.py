from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import crypto
from utils.logs import setup_logger

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger = setup_logger()

@app.on_event("startup")
async def startup_event():
    logger.info("Sistema de Previsão de Criptomoedas Iniciado")

app.include_router(crypto.router)
