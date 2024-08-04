from realTime_detection import classify_connection
from cli_interface import block_intrusion
from model_training import model, scaler

# Test scenarios
test_samples = [
    {'connection_duration': 5, 'signal_strength': -60, 'data_transfer_rate': 3, 'time_of_day': 10},
    {'connection_duration': 20, 'signal_strength': -40, 'data_transfer_rate': 10, 'time_of_day': 22},
    {'connection_duration': 7, 'signal_strength': -55, 'data_transfer_rate': 2, 'time_of_day': 15},
    {'connection_duration': 30, 'signal_strength': -30, 'data_transfer_rate': 15, 'time_of_day': 3},
    {'connection_duration': 1, 'signal_strength': -90, 'data_transfer_rate': 50, 'time_of_day': 3}
]

for sample in test_samples:
    prediction = classify_connection(model, scaler, sample)
    status = "Intrusion Detected!\n" if prediction == 1 else "Normal Connection"
    print(f"Data: {sample} => Status: {status}")
    if prediction == 1:
        block_intrusion(sample)
