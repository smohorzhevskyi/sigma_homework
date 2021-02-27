import plotly.graph_objs as go
from collections import defaultdict
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
alpha_vantage_url = os.getenv("SECTOR_URL")
response = requests.get(alpha_vantage_url)
json_str = json.dumps(response.json())

with open("data/sector/query.json", 'w') as f:
    f.write(json_str)

data_sectors = []
SECTORS = defaultdict(list)

with open("data/sector/query.json") as f:
    raw_data = json.load(f)
    del raw_data["Meta Data"]
    rank_names = raw_data.keys()

    for sectors in raw_data.values():
        for sector, value in sectors.items():
            SECTORS[sector].append(value)

for keys, values in dict(SECTORS).items():
    data_sectors.append(go.Bar(name=f"{keys}", x=list(rank_names), y=list([float(v.strip("%")) for v in values])))

# Проверка данных
if __name__ == '__main__':
    print(dict(SECTORS))
    print(data_sectors)
