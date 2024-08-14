import sys
import matplotlib.pyplot as plt
import pandas as pd
from realTime_detection import simulate_real_time_data, classify_connection
from model_training import model, scaler


# Block an intrusion (simulated)
def block_intrusion(sample):
    print(f"Blocking intrusion: {sample}")
    
def plot_data(data):
    plt.figure(figsize=(10, 6))
    plt.scatter(data['time_of_day'], data['connection_duration'], c=data['label'], cmap='coolwarm', alpha=0.5)
    plt.title('Bluetooth Connections')
    plt.xlabel('Time of Day')
    plt.ylabel('Connection Duration')
    plt.colorbar(label='Label (0: Normal, 1: Intrusion)')
    plt.show()
    
def cli_interaction():
     while True:
        print("1. Display Bluetooth Connections")
        print("2. Simulate Real-Time Detection")
        print("3. Exit\n")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            data = pd.read_csv('bluetooth_data2.csv')
            plot_data(data)
        elif choice == '2':
            # Simulate real-time data and classify
            for sample in simulate_real_time_data():
                prediction = classify_connection(model, scaler, sample)
                status = "Intrusion Detected!\n" if prediction == 1 else "Normal Connection\n"
                print(f"Data: {sample} => Status: {status}\n")
                if prediction == 1:
                    block_intrusion(sample)
        elif choice == '3':
            print("\nExiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.\n")

def main():
   cli_interaction()

if __name__ == "__main__":
    main()
