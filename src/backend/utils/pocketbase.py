import requests
import os
from tensorflow.keras.models import load_model
from utils import logs

POCKETBASE_URL = "https://sua-pocketbase-url.com"

def load_model_from_pocketbase(crypto: str, model_type: str):
    try:
        model_name = f"model_{model_type}_{crypto.lower()}.h5"
        model_path = f"app/models/{model_name}"
        
        if not os.path.exists(model_path):
            logger.info(f"Baixando modelo {model_type.upper()} para {crypto} da PocketBase")
            download_model(model_name)
        
        return load_model(model_path)
    except Exception as e:
        logger.error(f"Erro ao carregar o modelo {model_type.upper()} para {crypto}: {str(e)}")
        raise e

def download_model(model_name: str):
    url = f"{POCKETBASE_URL}/api/files/{model_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        model_path = f"app/models/{model_name}"
        with open(model_path, "wb") as f:
            f.write(response.content)
        logger.info(f"Modelo {model_name} baixado com sucesso")
    else:
        logger.error(f"Erro ao baixar o modelo: {response.status_code}")
        raise Exception("Erro ao baixar o modelo")
