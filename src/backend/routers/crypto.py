from fastapi import APIRouter, HTTPException
from utils.pocketbase import load_model_from_pocketbase
from utils.logs import logger
import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler

router = APIRouter()

@router.get("/predict/btc/gru")
async def predict_btc_gru():
    return await predict_price("BTC", "gru")

@router.get("/predict/sol/gru")
async def predict_sol_gru():
    return await predict_price("SOL", "gru")

@router.get("/predict/btc/lstm")
async def predict_btc_lstm():
    return await predict_price("BTC", "lstm")

@router.get("/predict/sol/lstm")
async def predict_sol_lstm():
    return await predict_price("SOL", "lstm")

async def predict_price(crypto: str, model_type: str):
    try:
        logger.info(f"Iniciando previsão para {crypto} usando {model_type.upper()}")

        model = load_model_from_pocketbase(crypto, model_type)
        logger.info(f"Modelo {model_type.upper()} para {crypto} carregado com sucesso")

        ticker = f"{crypto}-USD"
        data = yf.Ticker(ticker).history(period="2y", interval="1h")[["Close"]]

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

def generate_predictions(model, data):
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data)

    sequence_length = 60
    X = []
    for i in range(sequence_length, len(scaled_data)):
        X.append(scaled_data[i-sequence_length:i, 0])

    X = np.array(X).reshape((len(X), sequence_length, 1))

    predicted_prices = model.predict(X)

    predicted_prices = scaler.inverse_transform(predicted_prices)

    dates = pd.date_range(start=data.index[-1] + pd.Timedelta(hours=1), periods=len(predicted_prices), freq='H').strftime('%Y-%m-%d %H:%M:%S').tolist()

    return predicted_prices.flatten().tolist(), dates
