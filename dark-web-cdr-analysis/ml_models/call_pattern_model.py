# ml_models/call_pattern_model.py
import pandas as pd
from sklearn.cluster import KMeans

class CallPatternModel:
    def __init__(self):
        self.model = KMeans(n_clusters=3)

    def analyze_patterns(self, cdr_data):
        df = pd.DataFrame(cdr_data)
        self.model.fit(df[['call_duration', 'call_frequency']])
        df["cluster"] = self.model.labels_
        return df.to_dict(orient="records")

# Usage
# model = CallPatternModel()
# print(model.analyze_patterns(sample_cdr_data))
