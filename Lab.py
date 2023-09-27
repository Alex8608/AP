import requests
array=[]
url="https://www.cbr-xml-daily.ru/archive/2023/09/23/daily_json.js"
while url!="https://www.cbr-xml-daily.ru/archive/2023/02/03/daily_json.js":
    response=requests.get(url)
    data=response.json()
    array.append(f'{data["Date"][:10]},{data["Valute"]["USD"]["Value"]}')
    url="https:"+data["PreviousURL"]
array.reverse()
file=open("dataset.csv","w")
s="\n"
file.write(s.join(array))
file.close()