import pandas as pd
import numpy as np

def preprocess_data(file_path):
    data = pd.read_csv('bluetooth_data.csv')
    print(f"NaN values in dataset:\n{data.isna().sum()}")
    
    # Remove rows with NaN values
    data_cleaned = data.dropna()
    
    # Split features and target
    X = data_cleaned.iloc[:, :-1].values
    y = data_cleaned.iloc[:, -1].values
    
    return X, y