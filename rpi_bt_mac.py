import bluetooth
from datetime import datetime

def extract_bluetooth_data():
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
    else:
        print("No devices found.")
    return data_list

if __name__ == "__main__":
    extracted_data = extract_bluetooth_data()
    for data in extracted_data:
        print(data)
