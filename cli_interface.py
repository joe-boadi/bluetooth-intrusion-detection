import sys
import matplotlib.pyplot as plt

def plot_data(data):
    plt.figure(figsize=(10, 6))
    plt.scatter(data['time_of_day'], data['connection_duration'], c=data['label'], cmap='coolwarm', alpha=0.5)
    plt.title('Bluetooth Connections')
    plt.xlabel('Time of Day')
    plt.ylabel('Connection Duration')
    plt.colorbar(label='Label (0: Normal, 1: Intrusion)')
    plt.show()

def main():
    while True:
        print("1. Display Bluetooth Connections")
        print("2. Simulate Real-Time Detection")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            data = pd.read_csv('bluetooth_data.csv')
            plot_data(data)
        elif choice == '2':
            for sample in simulate_real_time_data():
                prediction = classify_connection(model, scaler, sample)
                status = "Intrusion Detected!" if prediction == 1 else "Normal Connection"
                print(f"Data: {sample} => Status: {status}")
        elif choice == '3':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
