from fastapi import APIRouter, HTTPException, Response 
import requests

router = APIRouter()

# URL base para o PocketBase
BASE_URL = "http://pocketbase:8090/api/files/u1owy14iqjskm4w/n5rubw8srjb4yec"


# Função para buscar o modelo no PocketBase
def fetch_model(model_filename: str):
    url = f"{BASE_URL}/{model_filename}"
    response = requests.get(url)

    if response.status_code == 200:
        # Retornar o conteúdo binário como uma resposta de bytes
        return Response(content=response.content, media_type="application/octet-stream")
    else:
        raise HTTPException(status_code=response.status_code, detail="Model not found")

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