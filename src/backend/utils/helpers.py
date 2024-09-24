from datetime import datetime
from sqlalchemy.orm import Session
from models import Prediction, Model, Features, Values

def add_prediction(db: Session, id_modelo: str, knr: str, prediction_result: int, real_result: int, 
                   best_buy_date: datetime, best_sell_date: datetime):
    new_prediction = Prediction(
        ID=f"pred_{knr}_{datetime.utcnow().timestamp()}",
        ID_modelo=id_modelo,
        KNR=knr,
        Prediction_result=prediction_result,
        Real_result=real_result,
        best_buy_date=best_buy_date,
        best_sell_date=best_sell_date
    )
    db.add(new_prediction)
    db.commit()
    db.refresh(new_prediction)
    return new_prediction

def add_model(db: Session, id_modelo: str, model_name: str, url_modelo: str):
    new_model = Model(
        ID_modelo=id_modelo,
        model=model_name,
        URL_modelo=url_modelo
    )
    db.add(new_model)
    db.commit()
    db.refresh(new_model)
    return new_model

def add_feature(db: Session, feature_name: str):
    new_feature = Features(
        name_feature=feature_name
    )
    db.add(new_feature)
    db.commit()
    db.refresh(new_feature)
    return new_feature

def add_value(db: Session, id_feature: int, id_prediction: str, id_modelo: str, value_feature: float):
    new_value = Values(
        ID_feature=id_feature,
        ID=id_prediction,
        ID_modelo=id_modelo,
        value_feature=value_feature
    )
    db.add(new_value)
    db.commit()
    db.refresh(new_value)
    return new_value

def get_predictions_by_model(db: Session, id_modelo: str):
    return db.query(Prediction).filter(Prediction.ID_modelo == id_modelo).all()

def get_prediction_by_id(db: Session, prediction_id: str):
    return db.query(Prediction).filter(Prediction.ID == prediction_id).first()

def get_best_dates_for_model(db: Session, id_modelo: str):
    predictions = db.query(Prediction).filter(Prediction.ID_modelo == id_modelo).all()
    return [{"best_buy_date": p.best_buy_date, "best_sell_date": p.best_sell_date} for p in predictions]
