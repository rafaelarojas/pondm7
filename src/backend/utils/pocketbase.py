import requests
import os
from tensorflow.keras.models import load_model
from fastapi import HTTPException
from utils import logs

# Configurações do PocketBase
POCKETBASE_URL = "http://pocketbase:8090"
COLLECTION_ID = "u1owy14iqjskm4w"
FIELD_ID = "n5rubw8srjb4yec"
FILES = {
    "btc": {
        "gru": "model_gru_btc_KbdmC8oKW3.h5",
        "lstm": "model_lstm_btc_baK6Tr7WtC.h5"
    },
    "sol": {
        "gru": "model_gru_sol_1afV8Ye8uC.h5",
        "lstm": "model_lstm_sol_JR3OEga8oO.h5"
    }
}

# Logger
logger = logs.setup_logger()

def authenticate_pocketbase():
    try:
        auth_data = {
            "identity": "teste@gmail.com",
            "password": "testeteste"
        }
        response = requests.post(f"{POCKETBASE_URL}/api/admins/auth-with-password", json=auth_data)

        if response.status_code == 200:
            logger.info("Authenticated successfully!")
            return response.json()["token"]
        else:
            logger.error(f"Authentication failed. Response: {response.text}")
            raise HTTPException(status_code=response.status_code, detail="Authentication failed.")
    except Exception as e:
        logger.error(f"Unexpected error during authentication: {e}")
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

# Autenticar com PocketBase e obter o token
try:
    pocketbase_token = authenticate_pocketbase()
except HTTPException as http_exc:
    logger.error(f"HTTP Exception: {http_exc.detail}")
except Exception as e:
    logger.error(f"Unexpected error: {str(e)}")

def load_model_from_pocketbase(crypto: str, model_type: str):
    """Carregar o modelo do PocketBase"""
    try:
        model_name = FILES[crypto][model_type]
        model_path = f"http://pocketbase:8090/api/files/u1owy14iqjskm4w/n5rubw8srjb4yec/model_lstm_sol_JR3OEga8oO.h5"

        # Verificar se o modelo já foi baixado
        if not os.path.exists(model_path):
            logger.info(f"Baixando modelo {model_type.upper()} para {crypto.upper()} da PocketBase")
            download_model(model_name)

        # Carregar o modelo do caminho local
        return load_model(model_path)

    except KeyError:
        logger.error(f"Modelo ou criptomoeda inválidos fornecidos: {crypto}, {model_type}")
        raise HTTPException(status_code=400, detail="Modelo ou criptomoeda inválidos.")
    except Exception as e:
        logger.error(f"Erro ao carregar o modelo {model_type.upper()} para {crypto.upper()}: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao carregar o modelo.")

def download_model(model_name: str):
    """Baixar o modelo da PocketBase e salvar localmente"""
    try:
        url = f"{POCKETBASE_URL}/api/files/{COLLECTION_ID}/{FIELD_ID}/{model_name}"
        response = requests.get(url, headers={"Authorization": f"Bearer {pocketbase_token}"})

        if response.status_code == 200:
            # Criar diretório de modelos se não existir
            os.makedirs("models", exist_ok=True)

            model_path = f"models/{model_name}"
            with open(model_path, "wb") as f:
                f.write(response.content)
            logger.info(f"Modelo {model_name} baixado com sucesso")
        else:
            logger.error(f"Erro ao baixar o modelo: {response.status_code}, Resposta: {response.text}")
            raise HTTPException(status_code=response.status_code, detail="Erro ao baixar o modelo.")

    except Exception as e:
        logger.error(f"Erro inesperado ao baixar o modelo {model_name}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao baixar o modelo: {str(e)}")