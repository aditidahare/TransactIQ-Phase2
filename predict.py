import joblib
import numpy as np
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "credit_risk_xgb_model.pkl"
model = joblib.load(MODEL_PATH)

def predict_risk(loan_amnt, term, int_rate, installment, annual_inc, dti, delinq_2yrs, revol_util, total_acc):
    input_data = np.array([[
        loan_amnt,
        term,
        int_rate,
        installment,
        annual_inc,
        dti,
        delinq_2yrs,
        revol_util,
        total_acc
    ]])

    prob = model.predict_proba(input_data)[0][1]

    if prob < 0.30:
        risk = "Low Risk"
    elif prob < 0.60:
        risk = "Medium Risk"
    else:
        risk = "High Risk"

    return prob, risk