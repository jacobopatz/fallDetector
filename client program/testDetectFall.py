import requests
from datetime import datetime, timezone

url = "http://0.0.0.0:8000/API/receive_message/"
# Changed URL to test on my local repo
# url = "http://localhost:8000/API/receive_message/" 


fall_data = {
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "has_fallen": True
}

response = requests.post(url, json=fall_data)

print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")
