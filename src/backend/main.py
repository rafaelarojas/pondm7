from fastapi import FastAPI
from predict import model_gru_btc, model_gru_sol, model_lstm_btc, model_lstm_sol

app = FastAPI()

@app.get("/predict")
def predict(input_data: dict):
    gru_btc = model_gru_btc.predict([input_data])
    gru_sol = model_gru_sol.predict([input_data])
    lstm_btc = model_lstm_btc.predict([input_data])
    lstm_sol = model_lstm_sol.predict([input_data])
    return {"result_model_gru_btc": gru_btc, "result_model_gru_sol": gru_sol, "result_model_lstm_btc:": lstm_btc, "result_model_lstm_sol:": lstm_sol}
