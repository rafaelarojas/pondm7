import tensorflow as tf
import os

def load_model(model_name):
    model_path = f"./ml_models/{model_name}"
    if os.path.exists(model_path):
        return tf.keras.models.load_model(model_path)
    else:
        raise FileNotFoundError(f"Modelo {model_name} nao encontrado")

def save_model(model, model_name):
    model_path = f"./ml_models/{model_name}"
    model.save(model_path)
