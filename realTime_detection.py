import time
import numpy as np
import pandas as pd
from model_training import model, scaler


def simulate_real_time_data(num_samples=10):
    for _ in range(num_samples):
        sample = {
            'connection_duration': np.random.exponential( scale=10 ),
            'signal_strength': np.random.normal( loc=-50, scale=10 ),
            'data_transfer_rate': np.random.exponential( scale=5 ),
            'time_of_day': np.random.uniform( low=0, high=24 )
        }
        yield sample
        time.sleep(1)  # Simulate real-time data stream

def classify_connection(model, scaler, sample):
    sample_df = pd.DataFrame([sample])
    sample_scaled = scaler.transform(sample_df)
    prediction = model.predict(sample_scaled)[0]
    return prediction
