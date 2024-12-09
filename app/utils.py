import pandas as pd

def clean_data(df):
    # Handle missing values, data anomalies, or transformations
    df.fillna(df.mean(), inplace=True)
    return df
