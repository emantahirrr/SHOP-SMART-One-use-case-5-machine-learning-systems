from fastapi import FastAPI
from pydantic import BaseModel, Field
import pandas as pd
import joblib
app = FastAPI(title="Churn Prediction API")
pipe = joblib.load("churn_v2.pkl")
from pydantic import BaseModel, Field
class Customer(BaseModel):
    user_id: int
    last_order_date: str
    first_order_date: str
    order_count: int = Field(..., ge=0)
    avg_order_value: float = Field(..., ge=0)
    avg_review_stars: float = Field(..., ge=0, le=5)
    days_since_last_order: int = Field(..., ge=0)
    tenure_days: int = Field(..., ge=0)
    order_velocity: float = Field(..., ge=0)
@app.post("/predict")
def predict(customer: Customer):
    X = pd.DataFrame([customer.model_dump()])
    p = float(pipe.predict_proba(X)[0, 1])
    return {"churn_probability": round(p, 3),"flag": p >= 0.30,"model_version": "churn_v2"}
