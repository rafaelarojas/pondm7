import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GRU
import os

def retrain_models():
    btc_data = yf.Ticker("BTC-USD").history(period="2y", interval="1h")
    sol_data = yf.Ticker("SOL-USD").history(period="2y", interval="1h")

    if btc_data.empty or sol_data.empty:
        raise ValueError("Não foi possível carregar os dados do Yahoo Finance.")

    # Pré-processamento para BTC
    btc_data = btc_data[["Close"]]
    btc_scaler = MinMaxScaler(feature_range=(0, 1))
    btc_scaled_data = btc_scaler.fit_transform(btc_data)

    btc_sequence_length = 60
    btc_X, btc_y = [], []
    
    for i in range(btc_sequence_length, len(btc_scaled_data)):
        btc_X.append(btc_scaled_data[i - btc_sequence_length : i, 0])
        btc_y.append(btc_scaled_data[i, 0])
    
    btc_X, btc_y = np.array(btc_X), np.array(btc_y)
    btc_X = np.reshape(btc_X, (btc_X.shape[0], btc_X.shape[1], 1))

    btc_model = Sequential()
    btc_model.add(GRU(units=100, return_sequences=True, input_shape=(btc_X.shape[1], 1)))
    btc_model.add(GRU(units=100))
    btc_model.add(Dense(1))

    btc_model.compile(optimizer="adam", loss="mean_squared_error")
    btc_model.fit(btc_X, btc_y, epochs=5, batch_size=32, verbose=1)

    btc_model_path = os.path.join('src', 'backend', 'ml_models', 'model_gru_btc.h5')
    btc_model.save(btc_model_path)

    sol_data = sol_data[["Close"]]
    sol_scaler = MinMaxScaler(feature_range=(0, 1))
    sol_scaled_data = sol_scaler.fit_transform(sol_data)

    sol_sequence_length = 60
    sol_X, sol_y = [], []
    
    for i in range(sol_sequence_length, len(sol_scaled_data)):
        sol_X.append(sol_scaled_data[i - sol_sequence_length : i, 0])
        sol_y.append(sol_scaled_data[i, 0])
    
    sol_X, sol_y = np.array(sol_X), np.array(sol_y)
    sol_X = np.reshape(sol_X, (sol_X.shape[0], sol_X.shape[1], 1))

    sol_model = Sequential()
    sol_model.add(GRU(units=100, return_sequences=True, input_shape=(sol_X.shape[1], 1)))
    sol_model.add(GRU(units=100))
    sol_model.add(Dense(1))

    sol_model.compile(optimizer="adam", loss="mean_squared_error")
    sol_model.fit(sol_X, sol_y, epochs=5, batch_size=32, verbose=1)

    sol_model_path = os.path.join('src', 'backend', 'ml_models', 'model_gru_sol.h5')
    sol_model.save(sol_model_path)

    return "Modelos treinados e salvos com sucesso."
