from fastapi import APIRouter, HTTPException, Response, Depends
import requests
import yfinance as yf
import tensorflow as tf
from datetime import datetime
from sqlalchemy.orm import Session
from db.db import get_db
from models.models import Log
import os

router = APIRouter()

# URL base para o PocketBase
BASE_URL = "http://pocketbase:8090/api/files/u1owy14iqjskm4w/n5rubw8srjb4yec"

# Função para buscar dados do yFinance até a data atual
def fetch_data(symbol: str, start_date: str):
    end_date = datetime.now().strftime('%Y-%m-%d')  # Obtém a data atual
    return yf.download(symbol, start=start_date, end=end_date)

# Função para retreinar modelos (exemplo usando LSTM)
def retrain_model(data, model_type="LSTM"):
    # Simplificado: aqui você pode carregar o modelo atual, treinar novamente, e salvá-lo
    model = tf.keras.Sequential([
        tf.keras.layers.LSTM(128, input_shape=(data.shape[1], 1)),
        tf.keras.layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    
    # Treinamento (exemplo simples)
    model.fit(data['Close'].values, data['Close'].values, epochs=5)

    # Retorna o modelo retreinado
    return model

# Função para atualizar o modelo no PocketBase
def update_model_in_pocketbase(model, filename):
    # Salvar o modelo localmente
    model.save(filename)

    # Excluir o modelo antigo do PocketBase e atualizar com o novo
    delete_response = requests.delete(f"{BASE_URL}/{filename}")
    if delete_response.status_code not in [200, 204]:
        raise HTTPException(status_code=delete_response.status_code, detail="Failed to delete old model")

    # Subir o novo modelo para o PocketBase
    files = {'file': open(filename, 'rb')}
    upload_response = requests.post(BASE_URL, files=files)
    if upload_response.status_code != 200:
        raise HTTPException(status_code=upload_response.status_code, detail="Failed to upload new model")

# Função para registrar logs no PostgreSQL
def log_to_db(db: Session, message: str):
    new_log = Log(timestamp=datetime.now(), message=message)
    db.add(new_log)
    db.commit()

# Função para buscar o modelo no PocketBase
def fetch_model(model_filename: str):
    url = f"{BASE_URL}/{model_filename}"
    response = requests.get(url)

    if response.status_code == 200:
        # Retornar o conteúdo binário como uma resposta de bytes
        return Response(content=response.content, media_type="application/octet-stream")
    else:
        raise HTTPException(status_code=response.status_code, detail="Model not found")

# Rota para retreinar todos os modelos
@router.post("/retrain-models")
async def retrain_models(db: Session = Depends(get_db)):
    # Registrar início do processo
    log_to_db(db, "Retreinamento dos modelos iniciado")

    # Obter dados recentes do yFinance até a data atual
    btc_data = fetch_data("BTC-USD", "2023-01-01")  # Exemplo: Obter dados desde 2023-01-01
    sol_data = fetch_data("SOL-USD", "2023-01-01")

    # Retreinar modelos
    try:
        # Retreinamento BTC
        model_btc = retrain_model(btc_data, model_type="LSTM")
        update_model_in_pocketbase(model_btc, "model_lstm_btc_baK6Tr7WtC.h5")

        # Retreinamento SOL
        model_sol = retrain_model(sol_data, model_type="LSTM")
        update_model_in_pocketbase(model_sol, "model_lstm_sol_JR3OEga8oO.h5")

        # Registrar sucesso no log
        log_to_db(db, "Retreinamento dos modelos concluído com sucesso")
        return {"message": "Modelos retreinados e atualizados com sucesso"}

    except Exception as e:
        # Registrar erro no log
        log_to_db(db, f"Erro durante o retreinamento: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro durante o retreinamento dos modelos")

# Rotas para cada modelo específico
@router.get("/model/gru/btc")
async def get_gru_btc_model():
    model_filename = "model_gru_btc_KbdmC8oKW3.h5"
    return fetch_model(model_filename)

@router.get("/model/lstm/btc")
async def get_lstm_btc_model():
    model_filename = "model_lstm_btc_baK6Tr7WtC.h5"
    return fetch_model(model_filename)

@router.get("/model/gru/sol")
async def get_gru_sol_model():
    model_filename = "model_gru_sol_1afV8Ye8uC.h5"
    return fetch_model(model_filename)

@router.get("/model/lstm/sol")
async def get_lstm_sol_model():
    model_filename = "model_lstm_sol_JR3OEga8oO.h5"
    return fetch_model(model_filename)

# Exemplo de rota para verificar o status do sistema
@router.get("/status")
async def get_status():
    return {"status": "Sistema de Previsão de Criptomoedas está ativo"}
