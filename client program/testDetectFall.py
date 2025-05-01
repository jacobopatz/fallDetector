import requests
from datetime import datetime, timezone
from tzlocal import get_localzone
url = "http://100.89.235.45:8000/API/receive_message/"
# Changed URL to test on my local repo
# url = "http://localhost:8000/API/receive_message/" 

tz = get_localzone()
fall_data = {
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "has_fallen": True
}

response = requests.post(url, json=fall_data)

print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")
print(datetime.now(timezone.utc).isoformat())
