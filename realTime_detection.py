import time
import numpy
import pandas as pd
from model_training import model, scaler


def simulate_real_time_data(num_samples=10):
    for _ in range(num_samples):
        sample = {
            'connection_duration': numpy.random.Generator.exponential(scale=10),
            'signal_strength': numpy.random.Generator.normal(loc=-50, scale=10),
            'data_transfer_rate': numpy.random.Generator.exponential(scale=5),
            'time_of_day': numpy.random.Generator.uniform(low=0, high=24)
        }
        yield sample
        time.sleep(1)  # Simulate real-time data stream

def classify_connection(model, scaler, sample):
    sample_df = pd.DataFrame([sample])
    sample_scaled = scaler.transform(sample_df)
    prediction = model.predict(sample_scaled)[0]
    return prediction

# Simulate real-time data and classify
for sample in simulate_real_time_data():
    prediction = classify_connection(model, scaler, sample)
    status = "Intrusion Detected!" if prediction == 1 else "Normal Connection"
    print(f"Data: {sample} => Status: {status}")
