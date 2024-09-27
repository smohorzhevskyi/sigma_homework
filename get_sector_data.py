import json
import os
from collections import defaultdict

import plotly.graph_objs as go
import requests

alpha_vantage_url = os.getenv("SECTOR_URL")
print(alpha_vantage_url)
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
