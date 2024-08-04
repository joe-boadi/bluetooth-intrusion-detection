import logging
import subprocess
import platform

logging.basicConfig(level=logging.INFO)

def block_intrusion(device_address):
    try:
        logging.info(f"Attempting to block device with address: {device_address}")
        
        os_type = platform.system().lower()
        if os_type == 'linux':
            # Linux-specific blocking command (replace with actual command)
            command = ['sudo', 'rfcomm', 'block', device_address]
        elif os_type == 'darwin':
            # macOS-specific blocking command (replace with actual command)
            command = ['sudo', 'blueutil', '--block', device_address]
        elif os_type == 'windows':
            # Windows-specific blocking command (replace with actual command)
            command = ['powershell', '-Command', f"Block-BTDevice -DeviceAddress '{device_address}'"]
        else:
            raise NotImplementedError(f"Blocking not implemented for {os_type}")

        result = subprocess.run(command, check=True, capture_output=True, text=True)
        logging.info(f"Device {device_address} blocked successfully. Output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to block device {device_address}: {e.stderr}")
    except Exception as e:
        logging.error(f"Unexpected error blocking device {device_address}: {e}")

# Example usage
sample_intrusion = {'device_address': '00:11:22:33:44:55', 'connection_duration': 30, 'signal_strength': -30, 'data_transfer_rate': 15, 'time_of_day': 3}
block_intrusion(sample_intrusion['device_address'])


# Actual Bluetooth blocking would require system-level permissions and would vary 
# depending on the operating 
# system and Bluetooth stack being used.
# The os.system() call is generally not recommended for security reasons. 
# In a real implementation, you'd want to use more secure methods like subprocess.run() 
# with proper input sanitization