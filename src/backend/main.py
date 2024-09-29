from fastapi import FastAPI
from routes import prediction
from utils.logs import setup_logger
from db.db import create_db_and_tables

app = FastAPI()

logger = setup_logger()

@app.on_event("startup")
async def startup_event():
    logger.info("Sistema Iniciado")
    create_db_and_tables()

app.include_router(prediction.router)
