from tensorflow.keras.models import load_model
from utils.pocketbase import download_model_from_pocketbase

def load_model_from_pocketbase(crypto: str, model_type: str):
    """Carregar o modelo GRU ou LSTM do PocketBase para a criptomoeda especificada."""
    try:
        # Determinar o nome do arquivo do modelo com base na criptomoeda e no tipo de modelo
        if crypto == "btc":
            if model_type == "gru":
                model_name = "model_gru_btc_KbdmC8oKW3.h5"
            elif model_type == "lstm":
                model_name = "model_lstm_btc_baK6Tr7WtC.h5"
        elif crypto == "sol":
            if model_type == "gru":
                model_name = "model_gru_sol_1afV8Ye8uC.h5"
            elif model_type == "lstm":
                model_name = "model_lstm_sol_JR3OEga8oO.h5"
        else:
            raise ValueError("Criptomoeda ou tipo de modelo inválido.")

        # Baixar o modelo da PocketBase
        model_path = download_model_from_pocketbase(model_name)

        # Carregar o modelo utilizando Keras
        model = load_model(model_path)

        return model

    except Exception as e:
        print(f"Erro ao carregar o modelo: {str(e)}")
        raise
