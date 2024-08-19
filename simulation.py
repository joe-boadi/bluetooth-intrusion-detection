import joblib
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

def block_intrusion(sample):
    print(f"Block intrusion: {sample}")

def load_model(file_name):
    model, scaler, feature_names = joblib.load(file_name)
    return model, scaler, feature_names

def generate_random_connection(feature_names):
    if np.random.random() < 0.1:  # 10% chance of anomaly
        return pd.DataFrame([np.random.rand(len(feature_names)) * 2], columns=feature_names)  # Anomalous data
    return pd.DataFrame([np.random.rand(len(feature_names))], columns=feature_names)  # Normal data

def display_connections(feature_names):
    # Generate some random connections for demonstration
    normal = [generate_random_connection(feature_names) for _ in range(50)]
    anomalous = [generate_random_connection(feature_names) for _ in range(50)]
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.scatter([x.iloc[0][0] for x in normal], [x.iloc[0][1] for x in normal], color='blue', label='Normal')
    plt.scatter([x.iloc[0][0] for x in anomalous], [x.iloc[0][1] for x in anomalous], color='red', label='Anomalous')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('Bluetooth Connections')
    plt.legend()
    plt.show()
    
def simulate_realtime_detection(model, scaler, feature_names, threshold=0.3):
    print(f"Simulating real-time detection with threshold {threshold}. Press Ctrl+C to stop.")
    try:
        while True:
            connection = generate_random_connection(feature_names)
            scaled_connection = scaler.transform(connection)
            
            try:
                probability = model.predict_proba(scaled_connection)[0][1]
            except IndexError:
                print("Error: Unable to get prediction probability. Skipping this connection.")
                continue
            
            if probability > threshold:
                print(f"ALERT: Potential unauthorized access detected! Confidence: {probability:.2f}")
                print("Blocking the connection...")
                # BLock Function to be invoked
                block_intrusion(scaled_connection)
            else:
                print(f"Normal connection detected. Confidence: {1-probability:.2f}")
            
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nSimulation stopped.")

def main_menu():
    while True:
        print("\nBluetooth Anomaly Detection System")
        print("1. Simulate Real-Time Detection")
        print("2. Display Information")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            simulate_realtime_detection(model, scaler, feature_names)
        elif choice == '2':
            display_connections(feature_names)
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    try:
        model, scaler, feature_names = load_model('bluetooth_anomaly_detector_new.joblib')
        main_menu()
    except Exception as e:
        print(f"An error occurred while loading the model: {str(e)}")
        print("Please ensure that the model file exists and is not corrupted.")