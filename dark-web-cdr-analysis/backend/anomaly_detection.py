# backend/anomaly_detection.py
import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(cdr_data):
    df = pd.DataFrame(cdr_data)
    model = IsolationForest(contamination=0.05)
    df["anomaly"] = model.fit_predict(df[["duration", "call_frequency"]])
    return df[df["anomaly"] == -1].to_dict(orient="records")
