import requests
import json

url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"

response = requests.get(url)
response.raise_for_status()

data = response.json()

with open("./data/cardinfo.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"{len(data['data'])} cartas salvas.")