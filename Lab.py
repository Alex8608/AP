import requests

url="https://www.cbr-xml-daily.ru/archive/2023/09/23/daily_json.js"

response=requests.get(url)
data=response.json()
print(data["Date"][:10], data["Valute"]["USD"]["Value"])
