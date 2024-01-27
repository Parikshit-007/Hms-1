import urllib.request
import json

url = "http://127.0.0.1:8000/api/patient_dashboard/api/patient/cnft/"

try:
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
        print(data)
except Exception as e:
    print(f"Error fetching data: {e}")
