# cdr_analysis/cdr_processor.py
import pandas as pd

def process_cdr(cdr_file):
    df = pd.read_csv(cdr_file)
    return df.to_dict(orient="records")
