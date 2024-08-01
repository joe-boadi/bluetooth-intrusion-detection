import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
num_samples = 1000
normal_ratio = 0.9  # 90% normal connections, 10% intrusions

# Generate features
connection_duration = np.random.exponential(scale=10, size=num_samples)
signal_strength = np.random.normal(loc=-50, scale=10, size=num_samples)
data_transfer_rate = np.random.exponential(scale=5, size=num_samples)
time_of_day = np.random.uniform(low=0, high=24, size=num_samples)

# Generate labels (0: normal, 1: intrusion)
labels = np.random.choice([0, 1], size=num_samples, p=[normal_ratio, 1 - normal_ratio])

# Create DataFrame
data = pd.DataFrame({
    'connection_duration': connection_duration,
    'signal_strength': signal_strength,
    'data_transfer_rate': data_transfer_rate,
    'time_of_day': time_of_day,
    'label': labels
})

# Save to CSV
data.to_csv('bluetooth_data.csv', index=False)
