import json
import datetime
from pathlib import Path
import requests

json_path = Path("/Kiani-X-Crawler/header.json")

def load_config(file_path):
    with open(file_path, 'r') as json_path:
        return json.load(json_path)


url = "https://x.com/search"

response = requests.get(url, params={"from": "@LauraLoomer",
                                     "since": (2020, 1, 1),
                                     "until": datetime.datetime.now().strftime("%Y-%m-%d"),
                                     },
                        headers=load_config(json_path)
                        )

print(response)





