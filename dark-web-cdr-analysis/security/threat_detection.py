# security/threat_detection.py
import pandas as pd
from sklearn.ensemble import IsolationForest

class ThreatDetection:
    def __init__(self):
        self.model = IsolationForest(contamination=0.02)

    def detect_threats(self, data):
        df = pd.DataFrame(data)
        df["threat"] = self.model.fit_predict(df[["anomaly_score"]])
        return df[df["threat"] == -1].to_dict(orient="records")

# Usage
# print(ThreatDetection().detect_threats(sample_logs))
