import requests

def date_conrol():
    while True:
        date=str(input())
        try:
            requests.get(f"https://www.cbr-xml-daily.ru/archive/{date}/daily_json.js").json()["Date"]
            return f"https://www.cbr-xml-daily.ru/archive/{date}/daily_json.js"
        except:
            print("Курс ЦБ РФ на данную дату не установлен\nУкажите другую дату: ")

print("Введите дату начала периода в формате yyyy/mm/dd: ")
url1=date_conrol()
print("Введите дату конца периода в формате yyyy/mm/dd: ")
url2=date_conrol()
array=[]
while url2!=url1:
    response=requests.get(url2)
    data=response.json()
    array.append(f'{data["Date"][:10]},{data["Valute"]["USD"]["Value"]}')
    url2="https:"+data["PreviousURL"]
array.append(f'{data["PreviousDate"][:10]},{data["Valute"]["USD"]["Previous"]}')
array.reverse()
file=open("./Lab1/dataset.csv","w")
s="\n"
file.write(s.join(array))
file.close()