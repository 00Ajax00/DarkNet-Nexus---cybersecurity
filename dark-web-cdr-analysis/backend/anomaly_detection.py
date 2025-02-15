# backend/anomaly_detection.py
import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(cdr_data):
    df = pd.DataFrame(cdr_data)
    
    # Ensure necessary features exist
    required_features = ["duration", "call_frequency", "location_entropy"]
    for feature in required_features:
        if feature not in df.columns:
            df[feature] = 0  # Default value

    # Train Isolation Forest with more features
    model = IsolationForest(contamination=0.03, n_estimators=200, random_state=42)
    df["anomaly"] = model.fit_predict(df[required_features])

    return df[df["anomaly"] == -1].to_dict(orient="records")
