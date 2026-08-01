"""
Qno6 - API Response Logger
Difficult words:
- API: Application Programming Interface
- log/logger: save records for later use
"""

import json
import time

# Simulated API response (normally comes from web request)
api_response = {
    "status": 200,
    "message": "success",
    "data": {"id": 1, "name": "Sample Item"}
}

log_entry = {
    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
    "response": api_response
}

with open("api_log.json", "a", encoding="utf-8") as file:
    file.write(json.dumps(log_entry) + "\n")

print("API response logged to api_log.json")
