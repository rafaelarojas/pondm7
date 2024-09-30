import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

# Set the title of the app
st.title("Crypto Price Prediction")

# Function to fetch predictions from the FastAPI backend
def fetch_predictions(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error fetching data")
        return None

# Sections for BTC
st.header("Bitcoin (BTC) Predictions")

# Buttons to fetch predictions from GRU and LSTM
if st.button("Fetch GRU Predictions"):
    btc_gru_url = "http://localhost:8000/btc/gru"
    btc_gru_data = fetch_predictions(btc_gru_url)
    
    if btc_gru_data:
        # Prepare data for plotting
        btc_gru_dates = pd.to_datetime(btc_gru_data["future_dates"])
        btc_gru_predictions = btc_gru_data["predictions"]
        
        # Plotting
        plt.figure(figsize=(10, 5))
        plt.plot(btc_gru_dates, btc_gru_predictions, label='GRU Predictions', color='blue')
        plt.title('BTC Price Predictions (GRU Model)')
        plt.xlabel('Date')
        plt.ylabel('Predicted Price')
        plt.xticks(rotation=45)
        plt.legend()
        st.pyplot(plt)

if st.button("Fetch LSTM Predictions"):
    btc_lstm_url = "http://localhost:8000/btc/lstm"
    btc_lstm_data = fetch_predictions(btc_lstm_url)
    
    if btc_lstm_data:
        btc_lstm_dates = pd.to_datetime(btc_lstm_data["future_dates"])
        btc_lstm_predictions = btc_lstm_data["predictions"]
        
        plt.figure(figsize=(10, 5))
        plt.plot(btc_lstm_dates, btc_lstm_predictions, label='LSTM Predictions', color='orange')
        plt.title('BTC Price Predictions (LSTM Model)')
        plt.xlabel('Date')
        plt.ylabel('Predicted Price')
        plt.xticks(rotation=45)
        plt.legend()
        st.pyplot(plt)

# Sections for SOL
st.header("Solana (SOL) Predictions")

if st.button("Fetch SOL GRU Predictions"):
    sol_gru_url = "http://localhost:8000/sol/gru"
    sol_gru_data = fetch_predictions(sol_gru_url)

    if sol_gru_data:
        sol_gru_dates = pd.to_datetime(sol_gru_data["future_dates"])
        sol_gru_predictions = sol_gru_data["predictions"]
        
        plt.figure(figsize=(10, 5))
        plt.plot(sol_gru_dates, sol_gru_predictions, label='GRU Predictions', color='green')
        plt.title('SOL Price Predictions (GRU Model)')
        plt.xlabel('Date')
        plt.ylabel('Predicted Price')
        plt.xticks(rotation=45)
        plt.legend()
        st.pyplot(plt)

if st.button("Fetch SOL LSTM Predictions"):
    sol_lstm_url = "http://localhost:8000/sol/lstm"
    sol_lstm_data = fetch_predictions(sol_lstm_url)

    if sol_lstm_data:
        sol_lstm_dates = pd.to_datetime(sol_lstm_data["future_dates"])
        sol_lstm_predictions = sol_lstm_data["predictions"]
        
        plt.figure(figsize=(10, 5))
        plt.plot(sol_lstm_dates, sol_lstm_predictions, label='LSTM Predictions', color='red')
        plt.title('SOL Price Predictions (LSTM Model)')
        plt.xlabel('Date')
        plt.ylabel('Predicted Price')
        plt.xticks(rotation=45)
        plt.legend()
        st.pyplot(plt)

# Logs section
st.header("Logs")

logs_url = "http://localhost:8000/logs"
logs_data = fetch_predictions(logs_url)

if logs_data:
    logs_df = pd.DataFrame(logs_data)
    st.table(logs_df)

