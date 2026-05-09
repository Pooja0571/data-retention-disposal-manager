import requests
from test_data import test_inputs

BASE_URL = "http://127.0.0.1:5000"

for data in test_inputs:
    print("\nTesting:", data)

    r1 = requests.post(f"{BASE_URL}/describe", json=data)
    print("Describe:", r1.json())

    r2 = requests.post(f"{BASE_URL}/recommend", json=data)
    print("Recommend:", r2.json())

    r3 = requests.post(f"{BASE_URL}/generate-report", json=data)
    print("Report:", r3.json())