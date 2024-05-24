import bluetooth
from datetime import datetime, timedelta
import time

def extract_bluetooth_data():
    retry_duration = timedelta(minutes=5)
    start_time = datetime.now()
    
    while datetime.now() - start_time < retry_duration:
        now = datetime.now()
        data_list = []
        
        devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)
        if devices:
            for addr, _ in devices:
                data = {
                    "Date": now.strftime("%d-%m-%Y"),
                    "Time": now.strftime("%H:%M:%S"),
                    "RecordNumber": int(now.timestamp()),
                    "MACaddress": addr,
                    "DetectorType": "BTWIFI"
                }
                data_list.append(data)
            return data_list  # Data found, return immediately
        
        else:
            print("No devices found. Retrying...")
            time.sleep(10)  # Wait for 10 seconds before retrying
    
    print("No devices found after 5 minutes. Exiting.")
    return []

if __name__ == "__main__":
    extracted_data = extract_bluetooth_data()
    for data in extracted_data:
        print(data)
