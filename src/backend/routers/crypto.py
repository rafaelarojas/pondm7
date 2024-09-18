from fastapi import APIRouter, HTTPException
from utils.pocketbase import load_model_from_pocketbase
from utils.logs import logger
import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler

router = APIRouter()

# Previsão para Bitcoin usando GRU
@router.get("/predict/btc/gru")
async def predict_btc_gru():
    return await predict_price("BTC", "gru")

# Previsão para Solana usando GRU
@router.get("/predict/sol/gru")
async def predict_sol_gru():
    return await predict_price("SOL", "gru")

# Previsão para Bitcoin usando LSTM
@router.get("/predict/btc/lstm")
async def predict_btc_lstm():
    return await predict_price("BTC", "lstm")

# Previsão para Solana usando LSTM
@router.get("/predict/sol/lstm")
async def predict_sol_lstm():
    return await predict_price("SOL", "lstm")

# Função genérica para carregar o modelo e gerar previsões
async def predict_price(crypto: str, model_type: str):
    try:
        # Log da operação
        logger.info(f"Iniciando previsão para {crypto} usando {model_type.upper()}")

        # Carregar o modelo da PocketBase
        model = load_model_from_pocketbase(crypto, model_type)
        logger.info(f"Modelo {model_type.upper()} para {crypto} carregado com sucesso")

        # Coletar dados históricos da criptomoeda
        ticker = f"{crypto}-USD"
        data = yf.Ticker(ticker).history(period="2y", interval="1h")[["Close"]]

        # Normalizar os dados e gerar previsões (Exemplo simplificado)
        predictions, dates = generate_predictions(model, data)
        
        logger.info(f"Previsões para {crypto} com {model_type.upper()} geradas com sucesso")
        
        return {
            "crypto": crypto,
            "model_type": model_type,
            "predictions": predictions,
            "dates": dates
        }
    except Exception as e:
        logger.error(f"Erro ao processar a previsão: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro no processamento da previsão")

# Função auxiliar para gerar previsões
def generate_predictions(model, data):
    # Normalizar os dados
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data)

    # Preparar os dados para o modelo (usando sequência de 60 horas de histórico)
    sequence_length = 60
    X = []
    for i in range(sequence_length, len(scaled_data)):
        X.append(scaled_data[i-sequence_length:i, 0])

    X = np.array(X).reshape((len(X), sequence_length, 1))

    # Fazer a previsão usando o modelo carregado
    predicted_prices = model.predict(X)

    # Inverter a normalização das previsões
    predicted_prices = scaler.inverse_transform(predicted_prices)

    # Preparar datas para as previsões
    dates = pd.date_range(start=data.index[-1] + pd.Timedelta(hours=1), periods=len(predicted_prices), freq='H').strftime('%Y-%m-%d %H:%M:%S').tolist()

    return predicted_prices.flatten().tolist(), dates
