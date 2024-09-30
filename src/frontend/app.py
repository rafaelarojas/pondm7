import streamlit as st
import pandas as pd
import requests
import plotly.graph_objects as go

st.title("CryptoPredictor")
st.markdown("<style>body {background-color: #1e1e1e;}</style>", unsafe_allow_html=True)

def fetch_predictions(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error fetching data")
        return None

def plot_predictions(dates, predictions, title, color):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=predictions, mode='lines+markers', name=title,
                             line=dict(color=color, width=2)))

    fig.update_layout(title=title,
                      title_font=dict(color='white'),
                      xaxis_title='Date',
                      xaxis_title_font=dict(color='white'),
                      yaxis_title='Predicted Price',
                      yaxis_title_font=dict(color='white'),
                      plot_bgcolor='#1e1e1e',
                      paper_bgcolor='#1e1e1e',
                      font_color='white',
                      legend=dict(bgcolor='black', bordercolor='black', borderwidth=1),
                      margin=dict(l=20, r=20, t=40, b=20))
    
    fig.update_xaxes(showgrid=True, gridcolor='gray', tickangle=45)
    fig.update_yaxes(showgrid=True, gridcolor='gray')
    
    st.plotly_chart(fig)

tab1, tab2 = st.tabs(["BTC-USD", "SOL-USD"])

with tab1:
    st.header("BTC-USD")
    st.image("https://cryptologos.cc/logos/bitcoin-btc-logo.png", width=50)

    btc_data = fetch_predictions("http://localhost:8000/btc/gru") 
    btc_lstm_data = fetch_predictions("http://localhost:8000/btc/lstm")
    
    st.subheader("$ " + str(btc_data['predictions'][-1]))
    st.write("Time to Sell: ", btc_data['best_sell_hour'])
    st.write("Time to Buy: ", btc_data['best_buy_hour'])

    if btc_data:
        btc_dates = pd.to_datetime(btc_data["future_dates"])
        btc_predictions = btc_data["predictions"]
        plot_predictions(btc_dates, btc_predictions, 'BTC-USD (GRU)', color='blue')

    if btc_lstm_data:
        btc_lstm_dates = pd.to_datetime(btc_lstm_data["future_dates"])
        btc_lstm_predictions = btc_lstm_data["predictions"]
        plot_predictions(btc_lstm_dates, btc_lstm_predictions, 'BTC-USD (LSTM)', color='orange')

    predictions_df = pd.DataFrame({
        "Date": btc_dates,
        "GRU Predictions": btc_predictions,
        "LSTM Predictions": btc_lstm_predictions
    })
    st.table(predictions_df)

with tab2:
    st.header("SOL-USD")
    st.image("https://cryptologos.cc/logos/solana-sol-logo.png", width=50)

    sol_data = fetch_predictions("http://localhost:8000/sol/gru")
    sol_lstm_data = fetch_predictions("http://localhost:8000/sol/lstm")
    
    st.subheader("$ " + str(sol_data['predictions'][-1]))
    st.write("Time to Sell: ", sol_data['best_sell_hour'])
    st.write("Time to Buy: ", sol_data['best_buy_hour'])

    if sol_data:
        sol_dates = pd.to_datetime(sol_data["future_dates"])
        sol_predictions = sol_data["predictions"]
        plot_predictions(sol_dates, sol_predictions, 'SOL-USD (GRU)', color='green')

    if sol_lstm_data:
        sol_lstm_dates = pd.to_datetime(sol_lstm_data["future_dates"])
        sol_lstm_predictions = sol_lstm_data["predictions"]
        plot_predictions(sol_lstm_dates, sol_lstm_predictions, 'SOL-USD (LSTM)', color='red')

    predictions_df = pd.DataFrame({
        "Date": sol_dates,
        "GRU Predictions": sol_predictions,
        "LSTM Predictions": sol_lstm_predictions
    })
    st.table(predictions_df)
