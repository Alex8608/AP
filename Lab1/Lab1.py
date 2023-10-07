import requests

def date_conrol():
    while True:
        date=str(input())
        try:
            requests.get(f"https://www.cbr-xml-daily.ru/archive/{date}/daily_json.js", headers={'User-agent':'Mozilla/5.0'}).json()["Date"]
            return f"https://www.cbr-xml-daily.ru/archive/{date}/daily_json.js"
        except:
            print("Курс ЦБ РФ на данную дату не установлен\nУкажите другую дату: ")
print("Введите дату конца периода в формате yyyy/mm/dd: ")
url=date_conrol()
while url!="https:":
    response=requests.get(url)
    data=response.json()
    print(data["Date"][:10])
    url="https:"+data["PreviousURL"]
    with open("./Lab1/dataset.csv","a") as file:
        file.write(f'{data["Date"][:10]},{data["Valute"]["USD"]["Value"]}\n')