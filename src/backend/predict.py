import requests

url = "http://localhost:8090//api/collections/models/records"
response = requests.get(url)
models = response.json()

model_gru_btc = models['items'][0]['model_gru_btc']
model_gru_sol = models['items'][0]['model_gru_sol']
model_lstm_btc = models['items'][0]['model_lstm_btc']
model_lstm_sol = models['items'][0]['model_lstm_sol']

download_model(model_gru_btc)
download_model(model_gru_sol)
download_model(model_lstm_btc)
download_model(model_lstm_sol)
