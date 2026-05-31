import requests

base_url = "http://apis.data.go.kr/1543061/abandonmentPublicService_v2"
url = base_url + "/abandonmentPublic_v2"
params = {
    "serviceKey": "16675a982576de9123a769831c2ca6c0b797733762ae5bd47bfed51688a8f5f1",
    "numOfRows": 20,
    "state": "notice",
    "upkind": "417000",
    "_type": "json"
}

res = requests.get(url, params=params)
data = res.json()
items = data['response']['body']['items']['item']
print(items)

from jinja2 import Template

with open("data/template.html", "r", encoding="utf-8") as f:
    template = Template(f.read())

html = template.render(animals=items)

with open("data/output.html", "w", encoding="utf-8") as f:
    f.write(html)