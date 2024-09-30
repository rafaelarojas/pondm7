from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
from datetime import timedelta
import yfinance as yf
from db.db import SessionLocal
from db.db import Log

app = FastAPI()

origins = [
    "http://localhost:8501",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_crypto_data(crypto_csv):
    data = pd.read_csv(crypto_csv, encoding='utf-8', parse_dates=['Datetime'], index_col='Datetime')
    close_prices = data[["Close"]]
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(close_prices)
    return data, close_prices, scaled_data, scaler

def generate_future_predictions(model, X_test, sequence_length, scaler, future_hours=96):
    last_sequence = X_test[-1]
    predictions = []
    
    for _ in range(future_hours):
        pred = model.predict(last_sequence.reshape(1, sequence_length, 1))
        predictions.append(pred[0, 0])
        last_sequence = np.append(last_sequence[1:], pred)[-sequence_length:]
        last_sequence = last_sequence.reshape(sequence_length, 1)
    
    return scaler.inverse_transform(np.array(predictions).reshape(-1, 1))

@app.get("/btc/gru")
def get_btc_gru_predictions():
    model = load_model("models/model_gru_btc.h5")
    data, close_prices, scaled_data, scaler = load_crypto_data("data/btc_data.csv")
    
    sequence_length = 60
    X_test = []
    for i in range(sequence_length, len(scaled_data)):
        X_test.append(scaled_data[i - sequence_length: i, 0])
    X_test = np.array(X_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    
    predictions = generate_future_predictions(model, X_test, sequence_length, scaler)
    
    last_date = data.index[-1]
    future_dates = pd.date_range(start=last_date + pd.Timedelta(hours=1), periods=96, freq='H')
    
    sell_hour_index = np.argmax(predictions)
    buy_hour_index = np.argmin(predictions)
    
    return {
        "future_dates": future_dates.tolist(),
        "predictions": predictions.flatten().tolist(),
        "best_sell_hour": future_dates[sell_hour_index],
        "best_buy_hour": future_dates[buy_hour_index],
    }

@app.get("/btc/lstm")
def get_btc_lstm_predictions():
    model = load_model("models/model_lstm_btc.h5")
    data, close_prices, scaled_data, scaler = load_crypto_data("data/btc_data.csv")
    
    sequence_length = 60
    X_test = []
    for i in range(sequence_length, len(scaled_data)):
        X_test.append(scaled_data[i - sequence_length: i, 0])
    X_test = np.array(X_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    
    predictions = generate_future_predictions(model, X_test, sequence_length, scaler)
    
    last_date = data.index[-1]
    future_dates = pd.date_range(start=last_date + pd.Timedelta(hours=1), periods=96, freq='H')
    
    sell_hour_index = np.argmax(predictions)
    buy_hour_index = np.argmin(predictions)
    
    return {
        "future_dates": future_dates.tolist(),
        "predictions": predictions.flatten().tolist(),
        "best_sell_hour": future_dates[sell_hour_index],
        "best_buy_hour": future_dates[buy_hour_index],
    }

@app.get("/sol/gru")
def get_sol_gru_predictions():
    model = load_model("models/model_gru_sol.h5")
    data, close_prices, scaled_data, scaler = load_crypto_data("data/sol_data.csv")
    
    sequence_length = 60
    X_test = []
    for i in range(sequence_length, len(scaled_data)):
        X_test.append(scaled_data[i - sequence_length: i, 0])
    X_test = np.array(X_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    
    predictions = generate_future_predictions(model, X_test, sequence_length, scaler)
    
    last_date = data.index[-1]
    future_dates = pd.date_range(start=last_date + pd.Timedelta(hours=1), periods=96, freq='H')
    
    sell_hour_index = np.argmax(predictions)
    buy_hour_index = np.argmin(predictions)
    
    return {
        "future_dates": future_dates.tolist(),
        "predictions": predictions.flatten().tolist(),
        "best_sell_hour": future_dates[sell_hour_index],
        "best_buy_hour": future_dates[buy_hour_index],
    }

@app.get("/sol/lstm")
def get_sol_lstm_predictions():
    model = load_model("models/model_lstm_sol.h5")
    data, close_prices, scaled_data, scaler = load_crypto_data("data/sol_data.csv")
    
    sequence_length = 60
    X_test = []
    for i in range(sequence_length, len(scaled_data)):
        X_test.append(scaled_data[i - sequence_length: i, 0])
    X_test = np.array(X_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    
    predictions = generate_future_predictions(model, X_test, sequence_length, scaler)
    
    last_date = data.index[-1]
    future_dates = pd.date_range(start=last_date + pd.Timedelta(hours=1), periods=96, freq='H')
    
    sell_hour_index = np.argmax(predictions)
    buy_hour_index = np.argmin(predictions)
    
    return {
        "future_dates": future_dates.tolist(),
        "predictions": predictions.flatten().tolist(),
        "best_sell_hour": future_dates[sell_hour_index],
        "best_buy_hour": future_dates[buy_hour_index],
    }
