import requests
import json
from pathlib import Path

# make an API request
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
r = requests.get(url)
path = Path(__file__).parent / "response.txt"
print(f"Status code: {r.status_code}")

response_dict = r.json()
response_string = json.dumps(response_dict, indent=4)
# print(response_string)
path.write_text(response_string)