# cdr_analysis/cluster_analysis.py
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

class CDRClusterAnalysis:
    def __init__(self, num_clusters=5):
        self.num_clusters = num_clusters
        self.scaler = StandardScaler()
        self.model = KMeans(n_clusters=self.num_clusters, random_state=42, n_init=10)

    def preprocess_data(self, df):
        """Cleans and normalizes CDR data for clustering."""
        features = ["call_duration", "frequency", "location_variance"]
        df = df.dropna(subset=features)
        df_scaled = self.scaler.fit_transform(df[features])
        return df_scaled

    def fit_clusters(self, df):
        """Fits K-Means clustering model to the CDR dataset."""
        processed_data = self.preprocess_data(df)
        self.model.fit(processed_data)
        df["cluster"] = self.model.predict(processed_data)
        return df

    def plot_clusters(self, df):
        """Visualizes clustering results."""
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=df["call_duration"], y=df["frequency"], hue=df["cluster"], palette="viridis")
        plt.title("CDR Cluster Analysis")
        plt.xlabel("Call Duration")
        plt.ylabel("Frequency")
        plt.show()

# Example Usage
if __name__ == "__main__":
    # Sample dataset (Replace with real CDR data)
    data = {
        "call_duration": np.random.randint(1, 120, 100),
        "frequency": np.random.randint(1, 50, 100),
        "location_variance": np.random.rand(100) * 10
    }
    df = pd.DataFrame(data)

    cdr_analyzer = CDRClusterAnalysis(num_clusters=4)
    clustered_df = cdr_analyzer.fit_clusters(df)
    print(clustered_df.head())

    cdr_analyzer.plot_clusters(clustered_df)
